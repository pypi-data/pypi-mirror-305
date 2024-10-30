hatch.env.virtual.VirtualEnvironment
====================================

.. currentmodule:: hatch.env.virtual

.. autoclass:: VirtualEnvironment
   :members:
   :show-inheritance:
   :inherited-members:

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~VirtualEnvironment.__init__
      ~VirtualEnvironment.activate
      ~VirtualEnvironment.app_status_creation
      ~VirtualEnvironment.app_status_dependency_installation_check
      ~VirtualEnvironment.app_status_dependency_state_check
      ~VirtualEnvironment.app_status_dependency_synchronization
      ~VirtualEnvironment.app_status_post_installation
      ~VirtualEnvironment.app_status_pre_installation
      ~VirtualEnvironment.app_status_project_installation
      ~VirtualEnvironment.apply_context
      ~VirtualEnvironment.apply_features
      ~VirtualEnvironment.check_compatibility
      ~VirtualEnvironment.command_context
      ~VirtualEnvironment.construct_pip_install_command
      ~VirtualEnvironment.create
      ~VirtualEnvironment.deactivate
      ~VirtualEnvironment.dependencies_in_sync
      ~VirtualEnvironment.dependency_hash
      ~VirtualEnvironment.enter_shell
      ~VirtualEnvironment.exists
      ~VirtualEnvironment.expand_command
      ~VirtualEnvironment.expose_uv
      ~VirtualEnvironment.find
      ~VirtualEnvironment.fs_context
      ~VirtualEnvironment.get_context
      ~VirtualEnvironment.get_env_var_option
      ~VirtualEnvironment.get_env_vars
      ~VirtualEnvironment.get_interpreter_resolver_env
      ~VirtualEnvironment.get_option_types
      ~VirtualEnvironment.install_project
      ~VirtualEnvironment.install_project_dev_mode
      ~VirtualEnvironment.join_command_args
      ~VirtualEnvironment.remove
      ~VirtualEnvironment.resolve_commands
      ~VirtualEnvironment.run_shell_command
      ~VirtualEnvironment.safe_activation
      ~VirtualEnvironment.sync_dependencies
      ~VirtualEnvironment.upgrade_possible_internal_python
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~VirtualEnvironment.PLUGIN_NAME
      ~VirtualEnvironment.app
      ~VirtualEnvironment.builder
      ~VirtualEnvironment.config
      ~VirtualEnvironment.context
      ~VirtualEnvironment.data_directory
      ~VirtualEnvironment.dependencies
      ~VirtualEnvironment.dependencies_complex
      ~VirtualEnvironment.description
      ~VirtualEnvironment.dev_mode
      ~VirtualEnvironment.env_exclude
      ~VirtualEnvironment.env_include
      ~VirtualEnvironment.env_vars
      ~VirtualEnvironment.environment_dependencies
      ~VirtualEnvironment.environment_dependencies_complex
      ~VirtualEnvironment.explicit_uv_path
      ~VirtualEnvironment.features
      ~VirtualEnvironment.installer
      ~VirtualEnvironment.isolated_data_directory
      ~VirtualEnvironment.matrix_variables
      ~VirtualEnvironment.metadata
      ~VirtualEnvironment.name
      ~VirtualEnvironment.parent_python
      ~VirtualEnvironment.pathsep
      ~VirtualEnvironment.platform
      ~VirtualEnvironment.platforms
      ~VirtualEnvironment.post_install_commands
      ~VirtualEnvironment.pre_install_commands
      ~VirtualEnvironment.project_root
      ~VirtualEnvironment.python_manager
      ~VirtualEnvironment.root
      ~VirtualEnvironment.scripts
      ~VirtualEnvironment.sep
      ~VirtualEnvironment.skip_install
      ~VirtualEnvironment.system_python
      ~VirtualEnvironment.use_uv
      ~VirtualEnvironment.uv_path
      ~VirtualEnvironment.verbosity
      ~VirtualEnvironment.virtual_env_cls
   
   