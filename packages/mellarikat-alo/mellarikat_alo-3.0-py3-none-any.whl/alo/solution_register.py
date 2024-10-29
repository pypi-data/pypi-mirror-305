import os
import sys
import json
import pyfiglet
import requests
import re
import yaml
import functools
import boto3
import shutil
import subprocess
import tarfile
import time
import docker
from copy import deepcopy
from collections.abc import Callable
from botocore.exceptions import ProfileNotFound, ClientError
from yaml import Dumper
from docker.errors import APIError

from alo.__version__ import __version__
from alo.exceptions import AloErrors, AloError
from alo.model import settings, load_model, SolutionInfo, SolutionMetadata, Description, EdgeConductorInterface, EdgeAppInterface, SolutionPipeline, \
    ParametersType


settings.update()
logger = settings.logger


########################
# user home
PROJECT_HOME = settings.home
SOLUTION_HOME = os.path.join(PROJECT_HOME, "solution")
REGISTER_ARTIFACT_PATH = os.path.join(PROJECT_HOME, ".register_artifacts")
REGISTER_SOURCE_PATH = os.path.join(PROJECT_HOME, ".register_source")
REGISTER_INTERFACE_PATH = os.path.join(PROJECT_HOME, ".register_interface")
REGISTER_WRANGLER_PATH = os.path.join(SOLUTION_HOME, "wrangler", "wrangler.py")
REGISTER_MODEL_PATH = os.path.join(PROJECT_HOME, ".register_model")
REGISTER_EXPPLAN = os.path.join(REGISTER_SOURCE_PATH, "solution", "experimental_plan.yaml")

SOLUTION_FILE = '.response_solution.json'
SOLUTION_INSTANCE_FILE = '.response_solution_instance.json'
STREAM_FILE = '.response_stream.json'
STREAM_RUN_FILE = '.response_stream_run.json'
STREAM_STATUS_FILE = '.response_stream_status.json'
STREAM_HISTORY_LIST_FILE = '.response_stream_history_list.json'
STREAM_LIST_FILE = '.response_stream_list.json'
INSTANCE_LIST_FILE = '.response_instance_list.json'
SOLUTION_LIST_FILE = '.response_solution_list.json'

SOLUTION_META = os.path.join(PROJECT_HOME, "solution_metadata.yaml")
ASSET_PACKAGE_DIR = ".package_list"
ASSET_PACKAGE_PATH = os.path.join(PROJECT_HOME, ".package_list")

AWS_CODEBUILD_ZIP_PATH = os.path.join(PROJECT_HOME, ".codebuild_solution_zip")
AWS_CODEBUILD_BUILD_SOURCE_PATH = os.path.join(AWS_CODEBUILD_ZIP_PATH, ".register_source")
AWS_CODEBUILD_BUILDSPEC_FILE = 'buildspec.yml'
AWS_CODEBUILD_S3_SOLUTION_FILE = "codebuild_solution"

SOLUTION_INFO_FILE_PATH = os.path.join(PROJECT_HOME, 'setting', 'solution_info.yaml')
INFRA_INFO_FILE_PATH = os.path.join(PROJECT_HOME, 'setting', 'infra_config.yaml')

########################
# alo home
SOURCE_HOME = os.path.dirname(os.path.abspath(__file__))
REGISTER_DOCKER_PATH = os.path.join(SOURCE_HOME, "Dockerfiles", "register")

AWS_CODEBUILD_BUILDSPEC_FORMAT_FILE = os.path.join(SOURCE_HOME, "ConfigFormats", "aws_codebuild_buildspec_format.yaml")
AWS_CODEBUILD_S3_PROJECT_FORMAT_FILE = os.path.join(SOURCE_HOME, "ConfigFormats", "aws_codebuild_s3_project_format.json")

SOLUTION_NAME_MAX_LEN = 100
AWS_SERVICE_CLIENT={}  # AWS client for reuse

TRAIN_INPUT_DATA_HOME = settings.history_path + "/latest/train/dataset/"
INFERENCE_INPUT_DATA_HOME = settings.history_path + "/latest/inference/dataset/"


def print_step(step_name, sub_title=False):
    """ print registration step info

    Args:
        step_name   (str): registration step name
        sub_title   (bool): whether to sub-title

    Returns: -

    """

    def wrapper(func):
        @functools.wraps(func)
        def decorator(*args, **kwargs):
            if not sub_title:
                logger.info("\n######################################################"
                            f'\n######    {step_name}'
                            "\n######################################################")
            else:
                logger.info(f'\n######  {step_name}')

            return func(*args, **kwargs)

        return decorator

    return wrapper


def find_latest_supported_ver(input_list):
    """ Find max value in input list.
        If value is string, convert it into float

    Args:
        input_list  (list): input list

    Returns:
        max_value   (float): max float value

    """
    max_value = None
    for item in input_list:
        converted_item = None
        try:
            converted_item = float(item)
        except ValueError:
            pass
        if isinstance(converted_item, float):
            if max_value is None or converted_item > max_value:
                max_value = converted_item
    return max_value


def load_config(template_path: str, load_func: Callable):
    """ check and load yaml into dict

    Args:
        template_path      (str): path or dict
        load_func     (Callable): yaml or json

    Returns:
        result_dict (dict): converted dict
    """
    try:
        with open(template_path) as f:
            return load_func(f)
    except Exception as e:
        raise AloErrors['ALO-SSA-002'](str(e), doc={'file': template_path}) from e


def make_art(msg):
    """ print title

    Args:
        msg (str): message

    Returns: -

    """
    ascii_art = pyfiglet.figlet_format(msg, font="slant")
    logger.info("*" * 80)
    logger.info(ascii_art)
    logger.info("*" * 80)


def get_alo_version():
    """ get alo version

    Args: -

    Returns:
        __version__ (str): alo version

    """
    if os.path.exists(os.path.join(PROJECT_HOME, '.git/HEAD')):
        with open(os.path.join(PROJECT_HOME, '.git/HEAD'), 'r') as f:
            ref = f.readline().strip()
        return ref.split('/')[-1] if ref.startswith('ref:') else ref
    else:
        return __version__


def _tar_dir(_path):
    """ compress dir into tar.gz

    Args:
        _path   (str): path for train_artifacts / inference_artifacts

    Returns:
        _save_path  (str): saved path

    """
    os.makedirs(REGISTER_ARTIFACT_PATH, exist_ok=True)
    os.makedirs(REGISTER_MODEL_PATH, exist_ok=True)
    if 'models' in _path:
        _save_path = os.path.join(REGISTER_MODEL_PATH, 'model.tar.gz')
        last_dir = 'models/'
    else:
        _save_path = os.path.join(REGISTER_ARTIFACT_PATH, f'{_path.strip(".")}.tar.gz')
        last_dir = _path
    tar = tarfile.open(_save_path, 'w:gz')
    for root, dirs, files in os.walk(PROJECT_HOME + _path):
        for file_name in files:
            # Since compression should start not from the absolute path \
            # beginning with /home but from within train_artifacts/ or models/
            tar.add(os.path.join(root, file_name), arcname=root.split(last_dir)[-1] + '/' + file_name)
    tar.close()
    return _save_path


__aic_session = requests.Session()


def call_aic(url: str, api_type: str, method: str = 'get', **kwargs):
    try:
        response = getattr(__aic_session, method)(url, **kwargs)
        if response.status_code == 200:
            logger.debug("API : [%s] %s")
            logger.info("[API][SUCCESS][%s] : %s", api_type, url)
            return response
        else:
            logger.error("[API][FAIL][%s] : %s", api_type, url)
            message = response.json().get('detail', {}).get('message') if response.json().get('detail', {}).get('message') else response.text
            raise AloErrors['ALO-SSA-001']("No success response message received from the server.\n  " + response.text,
                                           doc={'type': api_type,
                                                'api': url,
                                                'statusCode': response.status_code,
                                                'message': message})
    except AloError as e:
        raise e
    except Exception as e:
        raise AloErrors['ALO-SSA-004']("An error occurred when calling the server API.", doc={'api': url, 'error': str(e)}) from e


class NoAliasDumper(Dumper):
    def ignore_aliases(self, data):
        return True


class SolutionRegister:

    def __init__(self, user_id: str, user_pw: str):
        self.__user_id = user_id
        self.__user_pw = user_pw

        # solution_info
        self.__name = None
        self.__id = None
        self.__version_id = None
        self.__version_num = 1
        settings.update()

        self.aic = load_config(os.path.join(SOURCE_HOME, 'config', 'ai_conductor_api.json'), json.load)
        try:
            self.solution_info = load_model(SOLUTION_INFO_FILE_PATH, SolutionInfo)
        except AloError as e:
            if e.code == 'ALO-INI-003':
                raise AloErrors['ALO-SSA-002'](str(e), doc={'file': SOLUTION_INFO_FILE_PATH}) from e
        self.infra_config = load_config(INFRA_INFO_FILE_PATH, yaml.safe_load)
        self.infra_config["AIC_URI"] = self.infra_config["AIC_URI"].rstrip('/')

        self.aic_api = self.aic['API']

        aic_ver = self.get_aic_version()
        latest_supported_ver = max([float(v) for v in self.aic['VERSION'].keys()])
        if aic_ver > latest_supported_ver:
            logger.warning(f"AI Conductor version of {aic_ver} may not be supported.")
            aic_ver = latest_supported_ver
        aic_ver = f'{aic_ver}'
        self.register_solution_api = self.aic['VERSION'][aic_ver]['REGISTER_SOLUTION']
        self.sm_ver = self.aic['VERSION'][f'{aic_ver}']["SOLUTION_METADATA_VERSION"]

        self.aic_cookie = None
        self.workspace_id = None
        self.bucket_name = None
        self.ecr_name = None
        self._sol_me = SolutionMetadata(name="")

        self.sm_pipe_pointer = -1

        make_art("Register AI Solution !")

        self.get_cloud_client('s3')

    def get_api(self, name):
        return f'{self.infra_config["AIC_URI"]}/{self.aic_api[name]}'

    @print_step("Check Version", sub_title=True)
    def get_aic_version(self):
        """ Check AIC version and convert API

        Args: -

        Returns:
            version (float): AIP version

        """
        response = call_aic(self.get_api("VERSION"), "VERSION")
        response_json = response.json()
        version_str = response_json['versions'][0]['ver_str']
        logger.info(f"AIC version check: {version_str})")
        match = re.match(r'(\d+\.\d+)', version_str)
        return float(match.group(1)) if match else float(version_str)

    @print_step("Get/Check Cloud Service")
    def get_cloud_client(self, service_name: str):
        """ check aws s3 access, generate s3 client instance
        """
        if AWS_SERVICE_CLIENT.get(service_name):
            return AWS_SERVICE_CLIENT[service_name]

        profile_name = self.infra_config["AWS_KEY_PROFILE"]
        try:
            AWS_SERVICE_CLIENT[service_name] = boto3.Session(profile_name=profile_name).client(service_name, region_name=self.infra_config['REGION'])
        except ProfileNotFound:
            logger.info(f"[WARNING] AWS profile {profile_name} not found. Create session and s3 client without aws profile.")
            AWS_SERVICE_CLIENT[service_name] = boto3.client(service_name, region_name=self.infra_config['REGION'])
        except Exception as e:
            logger.error("The aws credentials are not available.")
            raise AloErrors['ALO-SSA-003']("The aws credentials are not available : " + str(e),
                                           doc={'awsProfile': profile_name, 'serviceName': service_name}) from e
        logger.info(f"[INFO] AWS region: {self.infra_config['REGION']}")
        return AWS_SERVICE_CLIENT[service_name]

    def login(self):
        """ login to AIC (get session).
            Login access is divided into cases where an account exists and where permissions exist.
            - case1: account O / authority X
            - case2: account O / authority single (ex cism-ws)
            - case3: account O / authority multi (ex cism-ws, magna-ws) - authority is depended on workspace
            - case4: account X  ()
        Returns: -

        """
        logger.info("Login to AI Conductor..")
        response_login = call_aic(self.get_api("LDAP_LOGIN") if self.infra_config["LOGIN_MODE"] == "ldap" else self.get_api("STATIC_LOGIN"),
                            'LOGIN', method='post', data=json.dumps({"login_id": self.__user_id, "login_pw": self.__user_pw})).json()
        ws_dict = {}
        for ws in response_login["workspace"]:
            ws_dict[ws["name"]] = ws["id"]  # {name: id}
        logger.info(f"Workspaces: {ws_dict}")
        if response_login['account_id']:
            logger.info('[SYSTEM] Success getting cookie from AI Conductor: %s', self.aic_cookie)
            logger.info('[SYSTEM] Success Login: %s', response_login)
            if self.infra_config["WORKSPACE_NAME"] in ws_dict:
                self.workspace_id = ws_dict[self.infra_config["WORKSPACE_NAME"]]
                logger.info(f'[SYSTEM] workspace ({self.infra_config["WORKSPACE_NAME"]}) is accessible')
            else:
                raise AloErrors['ALO-SSA-005']("Not found name of workspace",
                                               doc={'message': f'the workspace({self.infra_config["WORKSPACE_NAME"]}) is not accessible'})
        else:
            raise AloErrors['ALO-SSA-005']("Empty account_id.",
                                           doc={'message': "Not found user account information"})


    @print_step("Check ECR & S3 Resource")
    def load_system_resource(self):
        """ return available ecr, s3 uri

        Args: -

        Returns: -

        """
        response_json = call_aic(self.get_api("SYSTEM_INFO"), "SYSTEM_INFO", params={"workspace_id": self.workspace_id, "page_size": 100}).json()
        try:
            self.bucket_name = response_json["s3_bucket_name"]
            self.ecr_name = response_json["ecr_base_path"]
        except Exception as e:
            raise AloErrors['ALO-SSA-004']("Wrong format of << workspaces >> received from REST API.", doc={'api': self.get_api("SYSTEM_INFO"), 'error': str(e)}) from e

        logger.info(f"[INFO] S3_BUCUKET_URI: %s", response_json['s3_bucket_name'])
        logger.info(f"[INFO] ECR_URI: %s", response_json['ecr_base_path'])
        logger.info(f"[SYSTEM] AWS ECR: %s", self.ecr_name)
        logger.info(f"[SYSTEM] AWS S3 bucket: %s", self.bucket_name)

    @print_step("Solution Name Creation")
    def check_solution_name(self):
        """ Check if the solution name the user intends to register is available for use.
            If there is no duplicate name, it is recognized as a new solution.
            If the same name exists, switch to update mode and execute a solution update.

        Args:
            name (str): solution name

        Returns: -

        """
        name = self.solution_info.name
        if len(name.encode('utf-8')) > SOLUTION_NAME_MAX_LEN:
            raise AloErrors['ALO-SSA-006']("Please change name that is an invalid name.",
                                           doc={'name': name,
                                                'message': f"The length of solution name must be less than {SOLUTION_NAME_MAX_LEN}"})
        pattern = re.compile('^[a-zA-Z0-9-]+$')
        if not pattern.match(name):
            raise AloErrors['ALO-SSA-006']("Please change name that is an invalid name.",
                                           doc={'name': name,
                                                'message': "The only characters that can be used in the name of solution are uppercase "
                                                           "and lowercase English letters, dashes, and numbers. (ex. my-solution-v0)"})
        response_json = call_aic(self.get_api("SOLUTION_LIST"), "SOLUTION_LIST",
                            params={"workspace_id": self.workspace_id, "page_size": 0}).json()
        for idx, sol in enumerate(response_json['solutions']):
            logger.info("%02d, %s", idx + 1, sol['name'])
            if name == sol['name']:
                if self.solution_info.update:
                    self.__name, self.__id, self.__version_id = name, sol['id'], int(sol['versions'][0]['version_num']) + 1
                else:
                    raise AloErrors['ALO-SSA-006']("Please change name that is an invalid name.",
                                                   doc={'name': name, 'message': f"A name of solution already exists. Please change the name in {SOLUTION_INFO_FILE_PATH}."})
            # elif
        if self.solution_info.update and self.__name is None:
            raise AloErrors['ALO-SSA-006']("Please change name that is an invalid name.",
                                           doc={'name': name, 'message': f"Could not find solution name to update. Please check solution name in {SOLUTION_INFO_FILE_PATH}."})
        if not self.solution_info.update:
            self.__name = name

    def _init_solution_metadata(self):
        """ initialize solution metadata

        Args: -

        Returns: -

        """
        # Iterate over each directory and delete it if it exists.
        for dir_path in [REGISTER_ARTIFACT_PATH, REGISTER_SOURCE_PATH, REGISTER_INTERFACE_PATH]:
            if os.path.isdir(dir_path):
                logger.info(f"Removing directory: {dir_path}")
                shutil.rmtree(dir_path, ignore_errors=False)
                logger.info(f"Directory {dir_path} has been removed successfully.")
            else:
                logger.info(f"Directory {dir_path} does not exist, no action taken.")
        assert type(self.sm_ver) == float
        self._sol_me.metadata_version = self.sm_ver
        self._sol_me.name = self.__name
        self._save_yaml()

    @print_step("Set alo source code for docker container", sub_title=True)
    def _set_alo(self):
        """ copy alo components to register solution path

        Args: -

        Returns: -

        """
        alo_src = ['alo', 'solution', '.git']
        # initialize register source path
        if os.path.isdir(REGISTER_SOURCE_PATH):
            shutil.rmtree(REGISTER_SOURCE_PATH)
        os.mkdir(REGISTER_SOURCE_PATH)

        # copy things needed for docker
        shutil.copy2(os.path.join(SOURCE_HOME, 'Dockerfiles', 'main.py'), REGISTER_SOURCE_PATH)  # edgeapp의 docker 실행 경로를 위한 파일
        shutil.copy2(os.path.join(SOURCE_HOME, 'Dockerfiles', 'requirements.txt'), ASSET_PACKAGE_PATH)
        shutil.copy2(os.path.join(SOURCE_HOME, 'Dockerfiles', 'requirements.txt'), REGISTER_SOURCE_PATH)
        for item in alo_src:
            src_path = os.path.join(os.path.dirname(SOURCE_HOME), item)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, REGISTER_SOURCE_PATH)
                logger.info("copy file : %s -->  %s ", src_path, REGISTER_SOURCE_PATH)
            elif os.path.isdir(src_path):
                dst_path = os.path.join(REGISTER_SOURCE_PATH, os.path.basename(src_path))
                shutil.copytree(src_path, dst_path)
                logger.info("copy dir : %s -->  %s ", src_path, dst_path)

    @print_step("Set AI Solution Description")
    def set_description(self):
        """ insert solution description into solution metadata

        Args:
            description (dict): solution description (title, overview ..)

        Returns: -

        """
        description = {
            'title': self.__name,
            'alo_version': get_alo_version(),
            'contents_name': settings.experimental_plan.name,
            'contents_version': str(settings.experimental_plan.version),
            'inference_build_type': self.solution_info.inference.cpu,
            'overview': self.solution_info.overview,
            'detail': ""
        }
        self._sol_me.description = Description(**description)
        self._save_yaml()

    def _save_yaml(self):
        """ save into yaml file

        Args: -

        Returns: -

        """
        try:
            with open(os.path.join(PROJECT_HOME, 'solution_metadata.yaml'), 'w', encoding='utf-8') as yaml_file:
                yaml.dump(self._sol_me.model_dump(), yaml_file, allow_unicode=True, default_flow_style=False, Dumper=NoAliasDumper)
            logger.info(f"<< solution_metadata.yaml >> generated. - current version: v{self.sm_ver}")
        except Exception as e:
            raise AloErrors['ALO-SSA-007']("Failed to create file.",
                                           doc={'file': os.path.join(PROJECT_HOME, 'solution_metadata.yaml'), 'message': str(e)}) from e

    @print_step("Set Wrangler", sub_title=True)
    def set_wrangler(self):
        """ Reflect wrangler.py in the solution_metadata's code-to-string.
            Only ./wrangler/wrangler.py is supported.

        Args: -

        Returns: -

        """
        # FIXME wrangler spec-out
        try:
            with open(REGISTER_WRANGLER_PATH, 'r') as file:
                python_content = file.read()
            self._sol_me.wrangler_code_uri = python_content
            self._sol_me.wrangler_dataset_uri = ''
            self._save_yaml()
        except Exception as e:
            logger.warning("wrangler.py must be exist at this path: %s", REGISTER_WRANGLER_PATH)
            self._sol_me.wrangler_code_uri = ''
            self._sol_me.wrangler_dataset_uri = ''
            self._save_yaml()

    @print_step("Set Edge Condcutor & Edge App related metadata", sub_title=True)
    def set_edge(self, metadata_value={}):
        """ setup edge conductor, edge app related info to solution metadata

        Args:
            metadata_value (dict): edge related info from user

        Returns: -

        """
        if len(metadata_value) == 0:
            metadata_value = self.solution_info.contents_type.dict()
            metadata_value['inference_result_datatype'] = self.solution_info.inference.datatype
            metadata_value['train_datatype'] = self.solution_info.train.datatype

        self._sol_me.edgeconductor_interface = EdgeConductorInterface(**metadata_value)
        self._sol_me.edgeapp_interface = EdgeAppInterface(**{'single_pipeline': self.check_single_pipeline(), 'redis_server_uri': None, 'redis_db_number': 0})
        self._save_yaml()
        logger.info("[SUCCESS] contents_type --> solution_metadata updated")
        logger.info(f"edgeconductor_interface: %s", metadata_value)

    def check_single_pipeline(self):
        """check whether it is single pipeline solution
            single pipeline means that both train & inference occur in inference pipeline.

        Args: -

        Returns:
            Bool

        """
        phases = [phase for phase in ["inference", "train"] if getattr(settings.experimental_plan.solution, phase, None) is not None]
        if len(phases) == 2: # multi pipeline
            return False
        else: # single pipelien
            return True

    def set_solution_metadata(self):
        """ initialize soluiton metadata
        Args: -

        Returns: -

        """
        # init solution metadata
        self._init_solution_metadata()
        self._set_alo()
        self.set_description()
        self.set_wrangler()
        self.set_edge()

    def _sm_append_pipeline(self, pipeline_name):
        """ append pipeline to solution metadata

        Args:
            pipeline_name   (str): pipeline tobe appended

        Returns: -

        """
        self._sol_me.pipeline.append(SolutionPipeline(**{'type': pipeline_name}))
        # e.g. when adding an inference pipeline, change the pipeline attribute of the instance to 'inference'.
        self.pipeline = pipeline_name
        # pipeline pointer increases
        self.sm_pipe_pointer += 1
        self._save_yaml()

    @print_step("Set user parameters")
    def set_user_parameters(self, display_table=False):
        """ Display the parameters created in YAML and define their functionality.

        Args:
            display_table (bool): whether to show as table

        Returns:
            candidate_format (dict): candidate params format

        """
        exp_yaml = settings.experimental_plan.dict()
        params = deepcopy(exp_yaml['solution'])
        for pipe_name in ['train', 'inference']:
            if pipe_name in params:
                pipeline = params[pipe_name]
                sm_pipe_type = self._sol_me.pipeline[self.sm_pipe_pointer].type
                if sm_pipe_type == pipe_name:
                    subkeys = {}

                    selected_user_parameters = []
                    user_parameters = []
                    candidate_parameters = []  # Adding candidate parameters here
                    step_list = []
                    for step in pipeline['pipeline']:
                        output_data = {'step': step, 'args': {}}
                        selected_user_parameters.append(output_data.copy())
                        output_data = {'step': step, 'args': []}
                        user_parameters.append(output_data.copy())
                        step_list.append(step)

                        # Add candidate parameters
                        candidate_param = {'step': step, 'args': []}
                        candidate_param['args'] = [exp_yaml['solution']['function'][f'alo_{pipe_name}']['argument']]
                        candidate_parameters.append(candidate_param)

                    subkeys['selected_user_parameters'] = selected_user_parameters
                    subkeys['user_parameters'] = user_parameters
                    subkeys['candidate_parameters'] = candidate_parameters  # Include in subkeys
                    self._sol_me.pipeline[self.sm_pipe_pointer].parameters = ParametersType(**subkeys)
                    self._save_yaml()

        # display
        columns = ['pipeline', 'step', 'parameter', 'value']
        table_idx = 0
        self.candidate_format = {}
        for pipe_name in ['train', 'inference']:
            if pipe_name in params:
                self.candidate_format.update({pipe_name: []})
                step_idx = 0
                item_list = []
                for step in params[pipe_name]['pipeline']:
                    step_name = step
                    new_dict = {'step': step_name, 'args': []}
                    self.candidate_format[pipe_name].append(new_dict)
                    try:
                        for key, value in exp_yaml['solution']['function'][pipe_name]['argument'].items():
                            item = [pipe_name, step_name, key, value]
                            item_list.append(item)
                            new_dict2 = {'name': key, 'description': '', 'type': '', }
                            self.candidate_format[pipe_name][step_idx]['args'].append(new_dict2)
                            table_idx += 1
                    except:
                        self.candidate_format[pipe_name][step_idx]['args'].append({})
                        table_idx += 1
                    step_idx += 1

        if display_table:
            logger.info(columns)
            for i in item_list:
                logger.info(f"{i}")
        return self.candidate_format

    def set_pipeline_uri(self, mode, data_paths=[]):
        """ If one of the dataset, artifacts, or model is selected,
            generate the corresponding s3 uri and reflect this in the solution_metadata

        Args:
            mode        (str): dataset, artifacts, model
            data_paths  (list): data paths

        Returns:
            prefix_uri (str): prefix uri

        """
        prefix_uri = None
        if mode == "artifact":
            prefix_uri = "ai-solutions/" + self.__name + f"/v{self.__version_num}/" + self.pipeline + "/artifacts/"
            uri = {'artifact_uri': "s3://" + self.bucket_name + "/" + prefix_uri}
        elif mode == "dataset":
            prefix_uri = "ai-solutions/" + self.__name + f"/v{self.__version_num}/" + self.pipeline + "/data/"
            if len(data_paths) == 0:
                uri = {'dataset_uri': ["s3://" + self.bucket_name + "/" + prefix_uri]}
            else:
                uri = {'dataset_uri': []}
                data_path_base = "s3://" + self.bucket_name + "/" + prefix_uri
                for data_path_sub in data_paths:
                    uri['dataset_uri'].append(data_path_base + data_path_sub)
        elif mode == "model":
            prefix_uri = "ai-solutions/" + self.__name + f"/v{self.__version_num}/" + 'train' + "/artifacts/"
            if not self.check_single_pipeline():
                uri = {'model_uri': "s3://" + self.bucket_name + "/" + prefix_uri}
            else:
                uri = {'model_uri': None}
        setattr(self._sol_me.pipeline[self.sm_pipe_pointer], f'{mode}_uri', uri[f'{mode}_uri'])
        self._save_yaml()
        logger.info(f'[SUCCESS] Update solution_metadata.yaml')
        logger.info(f'pipeline type: %s, %s_uri: %s', self.pipeline, mode, uri)
        return prefix_uri

    def _s3_update(self, bucket_name, local_folder, s3_path, log_interval=50):
        """ upload data to s3 path.

        Args:
            bucket_name     (str): s3 bucket name
            local_folder    (str): local data directory name
            s3_path         (str): s3 path tobe uploaded
            log_interval    (int): data upload log interval

        Returns: -

        """
        if not s3_path:
            return
        if s3_path.endswith("/"):
            s3_path = s3_path.rstrip("/")
        for root, dirs, files in os.walk(local_folder):
            for idx, file in enumerate(files):
                data_path = os.path.join(root, file)
                try:
                    self.get_cloud_client('s3').upload_file(data_path, bucket_name, f"{s3_path}/{data_path[len(local_folder):]}")
                except Exception as e:
                    raise AloErrors['ALO-SSA-008']("Failed to upload/download.",
                                                   doc={'type': 'Upload',
                                                        'source': data_path,
                                                        'target': f's3://{bucket_name}/{s3_path}/{data_path[len(local_folder):]}',
                                                        'message': str(e)}) from e
                if idx % log_interval == 0:
                    logger.info(f"[SUCCESS] uploaded files to {bucket_name + '/' + s3_path} --- ( {idx} / {len(files)} )")

    def _s3_delete(self, bucket_name, s3_path, log_interval=50):
        """ delete s3 path

        Args:
            bucket_name (str): s3 bucket name
            s3_path     (str): s3 prefix path

        Returns: -

        """
        if not s3_path:
            return
        del_key = None
        try:
            objects_to_delete = self.get_cloud_client('s3').list_objects(Bucket=bucket_name, Prefix=s3_path)
            if 'Contents' in objects_to_delete:
                len_obj = len(objects_to_delete['Contents'])
                for idx, obj in enumerate(objects_to_delete['Contents']):
                    del_key = obj['Key']
                    self.get_cloud_client('s3').delete_object(Bucket=bucket_name, Key=del_key)
                    if idx % log_interval == 0:
                        logger.info(f'[SYSTEM] Deleted pre-existing S3 objects --- ( {idx} / {len_obj} )')
            del_key = s3_path
            self.get_cloud_client('s3').delete_object(Bucket=bucket_name, Key=s3_path)
        except Exception as e:
            raise AloErrors['ALO-SSA-008']("Failed to upload/download/delete.",
                                           doc={'type': 'Upload',
                                                'source': 'N/A',
                                                'target': f's3://{bucket_name}/{del_key}',
                                                'message': str(e)}) from e

    @print_step(f"Upload data to S3")
    def s3_upload_data(self):
        """ upload data file to s3

        Args: -

        Returns: -

        """
        if self.pipeline == 'train':
            local_folder = settings.history_path + "/latest/train/dataset/"
        elif  self.pipeline == 'inference':
            local_folder = settings.history_path + "/latest/inference/dataset/"
        logger.info(f'[SYSTEM] Start uploading data into S3 from local folder:\n {local_folder}')
        # update solution metadata
        data_uri_list = []
        for item in os.listdir(local_folder):
            sub_folder = os.path.join(local_folder, item)
            if os.path.isdir(sub_folder):
                data_uri_list.append(item + "/")
        s3_prefix_uri = self.set_pipeline_uri(mode="dataset", data_paths=data_uri_list)
        # delete & upload data to S3
        self._s3_delete(self.bucket_name, s3_prefix_uri)
        self._s3_update(self.bucket_name, local_folder, s3_prefix_uri)


    def s3_process(self, bucket_name, data_path, local_folder, s3_path, delete=True):
        """ delete and upload data to s3

        Args:
            bucket_name     (str): s3 bucket name
            data_path       (str): local data path
            local_folder    (str): local data directory name
            s3_path         (str): s3 path tobe uploaded
            delete          (bool): whether to delete pre-existing data in s3

        Returns: -

        """

        try:
            if delete:
                objects_to_delete = self.get_cloud_client('s3').list_objects(Bucket=bucket_name, Prefix=s3_path)
                if 'Contents' in objects_to_delete:
                    for obj in objects_to_delete['Contents']:
                        self.get_cloud_client('s3').delete_object(Bucket=bucket_name, Key=obj['Key'])
                        logger.info(f'[INFO] Deleted pre-existing S3 object: \n {obj["Key"]}')
                self.get_cloud_client('s3').delete_object(Bucket=bucket_name, Key=s3_path)
            self.get_cloud_client('s3').put_object(Bucket=bucket_name, Key=(s3_path +'/'))
            self.get_cloud_client('s3').upload_file(data_path, bucket_name, s3_path + data_path[len(local_folder):])
        except Exception as e:
            raise AloErrors['ALO-SSA-008']("Failed to upload/download/delete.",
                                           doc={'type': 'Upload',
                                                'source': local_folder,
                                                'target': f's3://{bucket_name}/{s3_path}',
                                                'message': str(e)}) from e
        uploaded_path = bucket_name + '/' + s3_path + data_path[len(local_folder):]
        logger.info(f"[SYSTEM] S3 object uploaded: {uploaded_path}")

    @print_step(f"Upload artifacts to S3")  # todo {self.pipeline}
    def s3_upload_artifacts(self):
        """ upload artifacts to s3

        Args: -

        Returns: -

        """

        s3_prefix_uri = self.set_pipeline_uri(mode="artifact")
        artifacts_path = _tar_dir(f"{self.pipeline}_artifacts")
        local_folder = os.path.split(artifacts_path)[0] + '/'
        logger.info(f'[INFO] Start uploading %s artifacts into S3 from local folder: \n%s', self.pipeline, local_folder)
        self.s3_process(self.bucket_name, artifacts_path, local_folder, s3_prefix_uri)
        shutil.rmtree(REGISTER_ARTIFACT_PATH, ignore_errors=True)
        if "inference" in self.pipeline:
            # upload inference artifacts
            # upload model.tar.gz to s3
            # (Note) The {model_uri} should be placed under the inference type, \
            # but the path should enter train instead of inference for the pipeline.
            if not self.check_single_pipeline():
                train_artifacts_s3_path = s3_prefix_uri.replace(f'v{self.__version_num}/inference', f'v{self.__version_num}/train')
                # model tar.gz saved local path
                model_path = _tar_dir("train_artifacts/models")
                local_folder = os.path.split(model_path)[0] + '/'
                logger.info(f'\n[SYSTEM] Start uploading << model >> into S3 from local folder: \n {local_folder}')
                # (Note) Since the train artifacts have already been uploaded to the same path, \
                # do not delete the object when uploading model.tar.gz.
                self.s3_process(self.bucket_name, model_path, local_folder, train_artifacts_s3_path, delete=False)
                # model uri into solution metadata
            try:
                # None (null) if single pipeline
                self.set_pipeline_uri(mode="model")
            except Exception as e:
                raise e
            finally:
                shutil.rmtree(REGISTER_MODEL_PATH, ignore_errors=True)

    def _set_dockerfile(self):
        """ setup dockerfile

        Args: -

        Returns: -

        """

        yaml_file = REGISTER_EXPPLAN
        shutil.copy(settings.config, REGISTER_EXPPLAN)
        with open(yaml_file, 'r') as file:
            yaml_content = yaml.safe_load(file)
        try:
            pipes = ['train', 'inference']
            del_pipe = pipes[(pipes.index(self.pipeline) + 1) % 2]
            if del_pipe in yaml_content['solution']:
                del yaml_content['solution'][del_pipe]
            with open(yaml_file, 'w') as file:
                yaml.safe_dump(yaml_content, file)
            dockerfile = f"{self.pipeline.capitalize()}Dockerfile"
            if os.path.isfile(os.path.join(PROJECT_HOME, dockerfile)):
                os.remove(os.path.join(PROJECT_HOME, dockerfile))
            shutil.copy(os.path.join(REGISTER_DOCKER_PATH, dockerfile), os.path.join(PROJECT_HOME, 'Dockerfile'))

            docker_location = '/framework/'

            def extract_integer(file_name):
                try:
                    return int(os.path.splitext(file_name)[0].split('_')[-1])
                except (ValueError, IndexError):
                    return float('inf')  # 기본값이나 원하는 값을 반환

            file_list = sorted(
                next(os.walk(ASSET_PACKAGE_PATH))[2],
                key=extract_integer
            )
            # install inference after train
            search_string = 'site_packages_location'
            with open(os.path.join(PROJECT_HOME, 'Dockerfile'), 'r', encoding='utf-8') as file:
                content = file.read()
            path = ASSET_PACKAGE_PATH.replace(PROJECT_HOME, "./")
            replace_string = '\n'.join([f"COPY {os.path.join(path, file)} {docker_location}" for file in file_list])
            requirement_files = [file for file in file_list if file.endswith('.txt')]
            pip_install_commands = '\n'.join([f"RUN pip3 install --no-cache-dir -r {docker_location}{file}" for file in requirement_files])
            if search_string in content:
                content = content.replace(search_string, replace_string + "\n" + pip_install_commands)
                with open(os.path.join(PROJECT_HOME, 'Dockerfile'), 'w', encoding='utf-8') as file:
                    file.write(content)
            logger.info(f"[SUCCESS] set Dockerfile for ({self.pipeline}) pipeline")
        except Exception as e:
            raise AloErrors['ALO-SSA-009']("Failed Dockerfile setting.", doc={'phase': self.pipeline, 'message': str(e)}) from e

    def _set_aws_ecr(self):
        """ set aws ecr

        Args: - 

        Returns: -

        """
        self.ecr_url = self.ecr_name.split("/")[0]
        ecr_scope = self.infra_config["WORKSPACE_NAME"].split('-')[0]
        self.ecr_repo = f'{self.ecr_name.split("/")[1]}/{ecr_scope}/ai-solutions/{self.__name}/{self.pipeline}/{self.__name}'
        self.ecr_full_url = f'{self.ecr_url}/{self.ecr_repo}'
        # if same ecr named exists, delete and re-create
        # During a solution update, only the own version should be deleted - deleting the entire repo would make the cache feature unusable.
        if self.solution_info.update is False:
            try:
                self.get_cloud_client('ecr').delete_repository(repositoryName=self.ecr_repo, force=True)
                logger.info(f"[SYSTEM] Repository {self.ecr_repo} already exists. Deleting...")
            except Exception as e:
                logger.info(f"[WARNING] Failed to delete pre-existing ECR Repository. \n {str(e)}")
        else:
            try:
                logger.info(f"Now in solution update mode. Only delete current version docker image.")
                resp_ecr_image_list = self.get_cloud_client('ecr').list_images(repositoryName=self.ecr_repo)
                logger.info(f"ecr image list response: \n {resp_ecr_image_list}")
                cur_ver_image = []
                for image in resp_ecr_image_list['imageIds']:
                    if 'imageTag' in image.keys():
                        if image['imageTag'] == f'v{self.__version_num}':
                            cur_ver_image.append(image)
                # In fact, during a solution update, there will likely be almost no already-created current version images.
                if len(cur_ver_image) != 0:
                    self.get_cloud_client('ecr').batch_delete_image(repositoryName=self.ecr_repo, imageIds=cur_ver_image)
            except Exception as e:
                raise AloErrors['ALO-SSA-010']('Failed to delete current version image.', doc={'type': 'Delete image', 'repository': self.ecr_repo, "message": str(e)})

        logger.info(f"[SYSTEM] target AWS ECR url: \n {self.ecr_full_url}")

    def _make_buildspec_commands(self):
        """ make buildspec for codebuild

        Args: -

        Returns:
            buildspec   (dict): codebuild buildspec

        """
        with open(AWS_CODEBUILD_BUILDSPEC_FORMAT_FILE, 'r') as file:
            buildspec = yaml.safe_load(file)
        pre_command = [f'aws ecr get-login-password --region {self.infra_config["REGION"]} | docker login --username AWS --password-stdin {self.ecr_url}']
        build_command = ['export DOCKER_BUILDKIT=1']
        if self.solution_info.update is True:
            # Download the previous version of the docker and utilize the cache when building the current version.
            pre_command.append(f'docker pull {self.ecr_full_url}:v{self.__version_num - 1}')
            build_command.append(
                f'docker build --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from {self.ecr_full_url}:v{self.__version_num - 1} -t {self.ecr_full_url}:v{self.__version_num} .')
        else:
            pre_command.append(f'aws ecr create-repository --repository-name {self.ecr_repo} --region {self.infra_config["REGION"]} --image-scanning-configuration scanOnPush=true')
            build_command.append(f'docker build --build-arg BUILDKIT_INLINE_CACHE=1 -t {self.ecr_full_url}:v{self.__version_num} .')
        post_command = [f'docker push {self.ecr_full_url}:v{self.__version_num}']
        buildspec['phases']['pre_build']['commands'] = pre_command
        buildspec['phases']['build']['commands'] = build_command
        buildspec['phases']['post_build']['commands'] = post_command
        del buildspec['phases']['install']
        return buildspec

    def _make_cross_buildspec_commands(self):
        """ make buildspec for codebuild (cross-build)

        Args: -

        Returns:
            buildspec   (dict): codebuild buildspec

        """
        # make buildspec for amd --> arm cross build
        with open(AWS_CODEBUILD_BUILDSPEC_FORMAT_FILE, 'r') as file:
            ## {'version': 0.2, 'phases': {'pre_build': {'commands': None}, 'build': {'commands': None}, 'post_build': {'commands': None}}}
            buildspec = yaml.safe_load(file)
        # runtime_docker_version = {'docker': AWS_CODEBUILD_DOCKER_RUNTIME_VERSION} ~ 19
        install_command = ['docker version',
                           'curl -JLO https://github.com/docker/buildx/releases/download/v0.4.2/buildx-v0.4.2.linux-amd64',
                           'mkdir -p ~/.docker/cli-plugins',
                           'mv buildx-v0.4.2.linux-amd64 ~/.docker/cli-plugins/docker-buildx',
                           'chmod a+rx ~/.docker/cli-plugins/docker-buildx',
                           'docker run --rm tonistiigi/binfmt --install all']
        # 'docker run --privileged --rm tonistiigi/binfmt --install all']
        pre_command = [f'aws ecr get-login-password --region {self.infra_config["REGION"]} | docker login --username AWS --password-stdin {self.ecr_url}']
        build_command = ['export DOCKER_BUILDKIT=1', \
                         'docker buildx create --use --name crossx']
        if self.solution_info.update is True:
            # Download the previous version of the docker and utilize the cache when building the current version.
            pre_command.append(f'docker pull {self.ecr_full_url}:v{self.__version_num - 1}')
            build_command.append(
                f'docker buildx build --push --platform=linux/amd64,linux/arm64 --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from {self.ecr_full_url}:v{self.__version_num - 1} -t {self.ecr_full_url}:v{self.__version_num} .')
        else:
            pre_command.append(f'aws ecr create-repository --repository-name {self.ecr_repo} --region {self.infra_config["REGION"]} --image-scanning-configuration scanOnPush=true')
            build_command.append(f'docker buildx build --push --platform=linux/amd64,linux/arm64 --build-arg BUILDKIT_INLINE_CACHE=1 -t {self.ecr_full_url}:v{self.__version_num} .')
        buildspec['phases']['install']['commands'] = install_command
        buildspec['phases']['pre_build']['commands'] = pre_command
        buildspec['phases']['build']['commands'] = build_command
        del buildspec['phases']['post_build']
        return buildspec

    def _make_codebuild_s3_project(self, bucket_uri, codebuild_role):
        """ make aws codebuild project (s3 type)

        Args:
            bucket_uri      (str): s3 bucket uri
            codebuild_role  (str): codebuiild role

        Returns:
            codebuild_project_json  (dict): codebuild project info.

        """
        with open(AWS_CODEBUILD_S3_PROJECT_FORMAT_FILE) as file:
            codebuild_project_json = json.load(file)
        codebuild_project_json['source']['location'] = bucket_uri + AWS_CODEBUILD_S3_SOLUTION_FILE + '.zip'
        codebuild_project_json['serviceRole'] = codebuild_role
        codebuild_project_json['environment']['type'] = self.infra_config["CODEBUILD_ENV_TYPE"]
        codebuild_project_json['environment']['computeType'] = self.infra_config["CODEBUILD_ENV_COMPUTE_TYPE"]
        codebuild_project_json['environment']['privilegedMode'] = False

        codebuild_project_json['tags'] = self.infra_config["REPOSITORY_TAGS"]
        codebuild_project_json['cache']['location'] = bucket_uri + 'cache'
        codebuild_project_json['logsConfig']['s3Logs']['location'] = bucket_uri + 'logs'
        codebuild_project_json['logsConfig']['s3Logs']['encryptionDisabled'] = True
        logger.info(f'codebuild project json: \n {codebuild_project_json}')
        return codebuild_project_json

    def _aws_codebuild(self):
        """ run aws codebuild for remote docker build & push

        Args: -

        Returns:
            codebuild_client    (object): aws codebuild client
            build_id            (str): codebuild id

        """
        # 0. create boto3 session and get codebuild service role arn
        codebuild_role = self.get_cloud_client('iam').get_role(RoleName = 'CodeBuildServiceRole')['Role']['Arn']

        # 1. make buildspec.yml
        if self.pipeline == 'train':
            buildspec = self._make_buildspec_commands()
        elif self.solution_info.inference.cpu != 'arm64' and self.pipeline == 'inference':
            buildspec = self._make_buildspec_commands()
        elif self.solution_info.inference.cpu == 'arm64' and self.pipeline == 'inference':
            buildspec = self._make_cross_buildspec_commands()
        # 2. make create-codebuild-project.json (trigger: s3)
        s3_prefix_uri = f"ai-solutions/{self.__name}/v{self.__version_num}/{self.pipeline}/codebuild/"
        bucket_uri = f"{self.bucket_name}/{s3_prefix_uri}"
        codebuild_project_json = self._make_codebuild_s3_project(bucket_uri, codebuild_role)
        # 3. make solution.zip (including buildspec.yml)
        # Except for the .package_list, all other files and folders are wrapped in a .register_source folder.
        # .codebuild_solution_zip directory init.
        if os.path.isdir(AWS_CODEBUILD_ZIP_PATH):
            shutil.rmtree(AWS_CODEBUILD_ZIP_PATH)
        os.makedirs(AWS_CODEBUILD_ZIP_PATH)
        # copy things needed for docker
        # The .package_list/{pipe}_pipeline, Dockerfile, solution_metadata.yaml (only for inference), \
        # and buildspec.yml files are located directly under the zip folder.
        # copy Dockerfile
        shutil.copy2(os.path.join(PROJECT_HOME, "Dockerfile"), AWS_CODEBUILD_ZIP_PATH)
        # copy solution_metdata.yaml (only when inference)
        if self.pipeline == 'inference':
            shutil.copy2(SOLUTION_META, AWS_CODEBUILD_ZIP_PATH)
        # REGISTER_SOURCE_PATH --> AWS_CODEBUILD_BUILD_SOURCE_PATH
        shutil.copytree(REGISTER_SOURCE_PATH, AWS_CODEBUILD_BUILD_SOURCE_PATH)
        shutil.copytree(ASSET_PACKAGE_PATH, os.path.join(AWS_CODEBUILD_ZIP_PATH, ASSET_PACKAGE_DIR))

        with open(os.path.join(AWS_CODEBUILD_ZIP_PATH, AWS_CODEBUILD_BUILDSPEC_FILE), 'w') as file: # save buildspec.yml
            yaml.safe_dump(buildspec, file)
        logger.info("[SUCCESS] Saved %s file for aws codebuild", AWS_CODEBUILD_BUILDSPEC_FILE)

        shutil.make_archive(os.path.join(PROJECT_HOME, AWS_CODEBUILD_S3_SOLUTION_FILE), 'zip', AWS_CODEBUILD_ZIP_PATH)
        logger.info("[SUCCESS] Saved %s.zip file for aws codebuild", AWS_CODEBUILD_S3_SOLUTION_FILE)

        # 4. s3 upload solution.zip
        local_file_path = os.path.join(PROJECT_HOME, AWS_CODEBUILD_S3_SOLUTION_FILE + '.zip')
        local_folder = os.path.split(local_file_path)[0] + '/'
        logger.info(f'\n[SYSTEM] Start uploading << {AWS_CODEBUILD_S3_SOLUTION_FILE}.zip >> into S3 from local folder:\n {local_folder}')
        self.s3_process(self.bucket_name, local_file_path, local_folder, s3_prefix_uri)
        # 5. run aws codebuild create-project
        codebuild_client = self.get_cloud_client('codebuild')
        # If a project with the same name already exists, delete it.
        ws_name = self.infra_config["WORKSPACE_NAME"].split('-')[0]
        # (Note) '/' not allowed in {project_name}
        project_name = f'{ws_name}_ai-solutions_{self.__name}_v{self.__version_num}'
        if project_name in codebuild_client.list_projects()['projects']:
            resp_delete_proj = codebuild_client.delete_project(name=project_name)
            logger.info(f"[INFO] Deleted pre-existing codebuild project: {project_name} \n {resp_delete_proj}")
        resp_create_proj = codebuild_client.create_project(name=project_name, **{k:codebuild_project_json[k]
                                                                                 for k in ['source', 'artifacts', 'cache', 'tags', 'environment', 'logsConfig', 'serviceRole']})
        # 6. run aws codebuild start-build
        if type(resp_create_proj)==dict and 'project' in resp_create_proj.keys():
            logger.info(f"[SUCCESS] CodeBuild create project response: \n {resp_create_proj}")
            proj_name = resp_create_proj['project']['name']
            assert type(proj_name) == str
            try:
                resp_start_build = codebuild_client.start_build(projectName = proj_name)
            except Exception as e:
                raise Exception(f"[FAIL] Failed to start-build CodeBuild project: {proj_name}") from e
            if type(resp_start_build)==dict and 'build' in resp_start_build.keys():
                build_id = resp_start_build['build']['id']
            else:
                raise Exception(f"[FAIL] << build id >> not found in response of codebuild - start_build")
        else:
            raise Exception(f"[FAIL] Failed to create CodeBuild project \n {resp_create_proj}")
        return build_id

    def get_user_password(self):
        """ get user and aws password

        Args: -

        Returns:
            user        (str): user
            password    (str): password

        """
        try:
            ecr_client = self.get_cloud_client('ecr')
            response = ecr_client.get_authorization_token()
            auth_data = response['authorizationData'][0]
            token = auth_data['authorizationToken']
            import base64
            user, password = base64.b64decode(token).decode('utf-8').split(':')
        except ClientError as e:
            raise Exception(f"An error occurred: {str(e)}") from e

        return user, password

    def buildah_login(self, password):
        """ buildah login

        Args:
            password    (str): aws configure password

        Returns: -

        """
        login_command = [
            'sudo', 'buildah', 'login',
            '--username', 'AWS',
            '--password-stdin',
            self.ecr_url
        ]
        try:
            p1 = subprocess.Popen(['echo', password], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(login_command, stdin=p1.stdout, stdout=subprocess.PIPE)
            ## Allow p1 to receive a SIGPIPE if p2 exits
            p1.stdout.close()
            output, _ = p2.communicate()
            if p2.returncode != 0:
                logger.error(output.decode('utf-8'))
            logger.info(f"Successfully logged in - {self.ecr_url} with Buildah")
        except subprocess.CalledProcessError as e:
            logger.info(f"An error occurred during Buildah login: \n {e.output.decode('utf-8')}")
        except RuntimeError as e:
            raise e

    def _ecr_login(self, is_docker):
        """ aws ecr login

        Args:
            is_docker   (bool): whether it is docker or buildah

        Returns: -

        """
        builder = "Docker" if is_docker else "Buildah"
        user, password = self.get_user_password()
        if is_docker:
            self.docker_client = docker.from_env(version='1.24')
            if not self.docker_client.ping():
                raise Exception("Docker connection error")
            try:
                login_results = self.docker_client.login(username=user, password=password, registry=self.ecr_url, reauth=True)
                logger.info(f'[SYSTEM] AWS ECR | {builder} login result: {login_results}')
                logger.info(f"[SUCCESS] logged in to {self.ecr_url}")
            except APIError as e:
                raise Exception(f"An error occurred during {builder} login: {e}") from e
        else:
            self.buildah_login(password)

    def _create_ecr_repository(self, tags):
        """ create ecr repository

        Args:
            tags   (list): tags dictionary list

        Returns: -

        """
        if self.solution_info.update is False:
            try:
                create_resp = self.get_cloud_client("ecr").create_repository(repositoryName=self.ecr_repo)
                repository_arn = create_resp.get('repository', {}).get('repositoryArn')
                resp = self.get_cloud_client("ecr").tag_resource(resourceArn=repository_arn, tags=tags)
                logger.info(f"[SYSTEM] AWS ECR create-repository response: ")
                logger.info(f"{resp}")
            except Exception as e:
                logger.error(f"Failed to AWS ECR create-repository:\n + {str(e)}")

    def _build_docker(self, is_docker):
        """ build docker image

        Args:
            is_docker   (bool): whether docker or buildah

        Returns: -

        """
        last_update_time = time.time()
        update_interval = 1
        log_file_path = f"{self.pipeline}_build.log"
        image_tag = f"{self.ecr_full_url}:v{self.__version_num}"
        if is_docker:
            try:
                with open(log_file_path, "w") as log_file:
                    for line in self.docker_client.api.build(path=PROJECT_HOME + '.', tag=image_tag, decode=True):
                        if 'stream' in line:
                            log_file.write(line['stream'])
                            if time.time() - last_update_time > update_interval:
                                sys.stdout.write('.')
                                sys.stdout.flush()
                                last_update_time = time.time()
                    sys.stdout.write(' Done!\n')
            except Exception as e:
                logger.info(f"An error occurred: {str(e)}")
        else:
            with open(log_file_path, "wb") as log_file:
                command = ['sudo', 'buildah', 'bud', '--isolation', 'chroot', '-t', image_tag, '.']
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in iter(process.stdout.readline, b''):
                    log_file.write(line)
                    if time.time() - last_update_time > update_interval:
                        sys.stdout.write('.')
                        sys.stdout.flush()
                        last_update_time = time.time()
                process.stdout.close()
                return_code = process.wait()
                if return_code == 0:
                    sys.stdout.write(' Done!\n')
                else:
                    raise Exception(f"[ERROR] Please check error log: {self.pipeline}_build.log")

    def _set_aws_ecr_skipbuild(self):
        """ set aws ecr when skipbuild is true

        Args: -

        Returns: -

        """
        self.ecr_url = self.ecr_name.split("/")[0]
        ecr_scope = self.infra_config["WORKSPACE_NAME"].split('-')[0]
        self.ecr_repo = self.ecr_name.split("/")[1] + '/' + ecr_scope + "/ai-solutions/" + self.__name + "/" + self.pipeline + "/" + self.__name
        self.ecr_full_url = self.ecr_url + '/' + self.ecr_repo
        logger.info(f"[SYSTEM] Target AWS ECR repository: \n {self.ecr_repo}")

    @print_step("Start setting AWS ECR")
    def make_docker(self, skip_build=False):
        """ Create a docker for upload to ECR.
            1. Copy the source code used in the experimental_plan to a temporary folder.
            2. Write the Dockerfile.
            3. Compile the Dockerfile.
            4. Upload the compiled docker file to ECR.
            5. Save the container URI to solution_metadata.yaml.

        Args:
            skip_build  (bool): whether to skip docker build

        Returns: -

        """
        assert self.infra_config['BUILD_METHOD'] in ['docker', 'buildah', 'codebuild']
        if not skip_build:
            is_remote = (self.infra_config['BUILD_METHOD'] == 'codebuild')
            is_docker = (self.infra_config['BUILD_METHOD'] == 'docker')
            if not is_remote:
                builder = "Docker" if is_docker else "Buildah"
            else:
                builder = "AWS Codebuild"
            # copy alo folders
            self._set_dockerfile()  # set docerfile
            self._set_aws_ecr()  # set aws ecr
            if not is_remote:
                self._ecr_login(is_docker=is_docker)
                logger.info("======= Create ECR Repository =======")
                self._create_ecr_repository(self.infra_config["REPOSITORY_TAGS"])
            else:
                pass
                # build docker image
            logger.info("Build image : %s", builder)
            if is_remote:
                try:
                    build_id = self._aws_codebuild()  # remote docker build & ecr push
                except Exception as e:
                    raise AloErrors['ALO-SSA-011']('Failed to save aws codebuild file.', doc={"message": str(e)}) from e
            else:
                start = time.time()
                self._build_docker(is_docker=is_docker)
                end = time.time()
                logger.info(f"{builder} build time : {end - start:.5f} sec")
        else:
            self._set_aws_ecr_skipbuild()

        if self.infra_config["BUILD_METHOD"] == "codebuild":
            return build_id
        else:
            return None

    def _remove_docker_image(self, is_docker):

        """ Remove docker image """

        image_tag = f"{self.ecr_full_url}:v{self.__version_num}"
        if is_docker:
            try:
                self.docker_client.images.remove(image=image_tag, force=True)
                logger.info(f"Image {image_tag} removed successfully.")
            except docker.errors.ImageNotFound as e:
                raise Exception(f"Image {image_tag} not found.") from e
            except Exception as e:
                raise Exception(f"An error occurred: {str(e)}") from e
        else:
            try:
                command = ['sudo', 'buildah', 'rmi', image_tag]
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                if process.returncode == 0:
                    logger.info(f"Image {image_tag} removed successfully.")
                else:
                    raise Exception(f"Failed to remove image {image_tag}. Error: {stderr.decode().strip()}")

            except Exception as e:
                raise Exception(f"An error occurred: {str(e)}") from e

    @print_step(f"push container", sub_title=True)
    def docker_push(self):
        """ docker push to ecr

        Args: -

        Returns: -

        """
        image_tag = f"{self.ecr_full_url}:v{self.__version_num}"
        if self.infra_config['BUILD_METHOD'] == 'docker':
            try:
                response = self.docker_client.images.push(image_tag, stream=True, decode=True)
                for line in response:
                    sys.stdout.write('.')
                    sys.stdout.flush()
                logger.info("docker push done")
            except Exception as e:
                logger.info(f"Exception occurred: {str(e)}")
        elif self.infra_config['BUILD_METHOD'] == 'buildah':
            subprocess.run(['sudo', 'buildah', 'push', f'{self.ecr_full_url}:v{self.__version_num}'])
            subprocess.run(['sudo', 'buildah', 'logout', '-a'])
        elif self.infra_config['BUILD_METHOD'] == 'codebuild':
            pass

    def _set_container_uri(self):
        """ set docker container uri

        Args: -

        Returns: -

        """
        data = {'container_uri': f'{self.ecr_full_url}:v{self.__version_num}'}
        self._sol_me.pipeline[self.sm_pipe_pointer].__dict__.update(data)
        logger.info(f"[SYSTEM] Completes setting << container_uri >> in solution_metadata.yaml:")
        logger.info(f"container_uri: {data['container_uri']}")
        self._save_yaml()

    def run_pipeline(self, pipe):
        """ upload data to s3, docker push to ecr ..

        Args:
            pipe    (str): pipeline name

        Returns:
            codebuild_client    (object): aws codebuild client
            build_id            (str): codebuild id

        """
        self._sm_append_pipeline(pipeline_name=pipe)
        self.set_user_parameters()
        self.s3_upload_data()
        self.s3_upload_artifacts()
        build_id = self.make_docker(False)
        self.docker_push()
        self._set_container_uri()
        return build_id

    def _download_codebuild_s3_log(self, resp_batch_get_builds):
        """ download codebuild log from s3

        Args:
            resp_batch_get_builds   (dict): codebuild status

        Returns: -

        """
        s3_bucket, file_key, local_file_path = None, None, None
        try:
            codebuild_id = resp_batch_get_builds['builds'][0]['id']
            s3_log_path = resp_batch_get_builds['builds'][0]['logs']['s3LogsArn'].split(':::')[-1]
            s3_bucket, file_key = s3_log_path.split('/', maxsplit=1)
            local_file_path = os.path.join(PROJECT_HOME, f"codebuild_fail_log_{codebuild_id}.gz".replace(':', '_'))
            self.get_cloud_client('s3').download_file(s3_bucket, file_key, local_file_path)
            logger.info(f'\n Downloaded: s3://{s3_bucket}/{file_key} \n --> {local_file_path} \n Please check the log!')
        except Exception as e:
            raise AloErrors['ALO-SSA-008']("Failed to download codebuild fail log.",
                                           doc={'type': 'Download',
                                                'source': f's3://{s3_bucket}/{file_key}',
                                                'target': local_file_path,
                                                'message': str(e)}) from e

    def _batch_get_builds(self, build_id, status_period=30):
        """ batch get codebuild status

        Args:
            build_id            (str): codebuild id
            status_period       (int): check status period

        Returns:
            build_status    (str): codebuild status

        """
        build_status = None
        while True:
            resp_batch_get_builds = self.get_cloud_client('codebuild').batch_get_builds(ids=[build_id])
            if type(resp_batch_get_builds) == dict and 'builds' in resp_batch_get_builds.keys():
                logger.info(f'Response-batch-get-builds: \n {resp_batch_get_builds}')
                logger.info('-------------------------------------------------------------------------------- \n')
                # assert len(resp_batch_get_builds) == 1
                # Since there will only be one build per pipeline, only one item is embedded in the ids list.
                build_status = resp_batch_get_builds['builds'][0]['buildStatus']
                # 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED'
                if build_status == 'SUCCEEDED':
                    logger.info(f"[SUCCESS] Completes remote build with AWS CodeBuild")
                    break
                elif build_status == 'IN_PROGRESS':
                    logger.info(f"[IN PROGRESS] In progress.. remote building with AWS CodeBuild")
                    time.sleep(status_period)
                else:
                    self._download_codebuild_s3_log(resp_batch_get_builds)
                    raise AloErrors['ALO-SSA-011'](f'[FAIL] Failed to remote build with AWS CodeBuild.', doc={"message": f"Build Status {build_status}, Check codebuild_fail_log_xxxx.gz"})
            else:
                raise AloErrors['ALO-SSA-011'](f'[FAIL] The AWS CodeBuild execution request response result is abnormal.', doc={"message": "Contact to ALO admin."})
        return build_status

    @print_step("Register AI solution")
    def register_solution(self):
        """ Differentiated into regular registration and solution update.
            If solution_info["solution_update"] is True, proceed with the update process.

        Args: -

        Returns: -

        """
        self.register_solution_api["metadata_json"] = self._sol_me.model_dump()
        data = json.dumps(self.register_solution_api)
        if self.solution_info.update:
            solution_params = {
                "solution_id": self.__id,
                "workspace_id": self.workspace_id
            }
            api = self.get_api("REGISTER_SOLUTION") + f"/{self.__id}/version"
        else:
            solution_params = {
                "workspace_id": self.workspace_id
            }
            api = self.get_api("REGISTER_SOLUTION")
        response_solution = call_aic(api, "REGISTER_SOLUTION", method="post", params=solution_params, data=data)
        logger.info(f"[INFO] AI solution register response: \n {response_solution}")
        # delete local docker image 
        if self.infra_config['BUILD_METHOD'] != 'codebuild':
            try:
                if os.path.exists(REGISTER_INTERFACE_PATH):
                    shutil.rmtree(REGISTER_INTERFACE_PATH)
                os.mkdir(REGISTER_INTERFACE_PATH)

                is_docker = (self.infra_config['BUILD_METHOD'] == 'docker')
                self._remove_docker_image(is_docker)
                path = os.path.join(REGISTER_INTERFACE_PATH, SOLUTION_FILE)
                with open(path, 'w') as f:
                    json.dump(response_solution, f, indent=4)
                    logger.info(f"[SYSTEM] save register result to {path}")
            except Exception as e:
                logger.error(f"Failed to generate interface directory while registering solution: \n {str(e)}")

    def register(self):
        """ run solution registraion flow API

        Args: -

        Returns: -

        """
        self.login()
        # set solution name
        self.check_solution_name()
        # load s3, ecr info
        self.load_system_resource()
        # FIXME set description & wrangler (spec-out)
        self.set_solution_metadata()
        # run solution registration pipeline
        pipelines = ["train", "inference"]
        codebuild_run_meta = {}
        for pipe in pipelines:
            if self.solution_info.inference and self.solution_info.inference.only and pipe == 'train':
                continue
            build_id = self.run_pipeline(pipe)
            codebuild_run_meta[pipe] = build_id
        # wait until codebuild finish for each pipeline
        for pipe in codebuild_run_meta:
            if codebuild_run_meta[pipe] is not None:
                self._batch_get_builds(codebuild_run_meta[pipe])
        # Since it is before solution registration, code to delete the solution cannot be included.
        self.register_solution()

    def update(self):
        print("implements update. #todo", file=sys.stderr)
        return
        self.login()


    def delete(self, name):
        print(f"implements delete {name}. #todo", file=sys.stderr)
        return
        self.login()

