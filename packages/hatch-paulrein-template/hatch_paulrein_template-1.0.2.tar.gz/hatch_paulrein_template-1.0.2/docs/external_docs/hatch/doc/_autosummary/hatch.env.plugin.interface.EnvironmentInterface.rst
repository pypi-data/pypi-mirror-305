hatch.env.plugin.interface.EnvironmentInterface
===============================================

.. currentmodule:: hatch.env.plugin.interface

.. autoclass:: EnvironmentInterface
   :members:
   :show-inheritance:
   :inherited-members:

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~EnvironmentInterface.__init__
      ~EnvironmentInterface.activate
      ~EnvironmentInterface.app_status_creation
      ~EnvironmentInterface.app_status_dependency_installation_check
      ~EnvironmentInterface.app_status_dependency_state_check
      ~EnvironmentInterface.app_status_dependency_synchronization
      ~EnvironmentInterface.app_status_post_installation
      ~EnvironmentInterface.app_status_pre_installation
      ~EnvironmentInterface.app_status_project_installation
      ~EnvironmentInterface.apply_context
      ~EnvironmentInterface.apply_features
      ~EnvironmentInterface.check_compatibility
      ~EnvironmentInterface.command_context
      ~EnvironmentInterface.construct_pip_install_command
      ~EnvironmentInterface.create
      ~EnvironmentInterface.deactivate
      ~EnvironmentInterface.dependencies_in_sync
      ~EnvironmentInterface.dependency_hash
      ~EnvironmentInterface.enter_shell
      ~EnvironmentInterface.exists
      ~EnvironmentInterface.expand_command
      ~EnvironmentInterface.find
      ~EnvironmentInterface.fs_context
      ~EnvironmentInterface.get_context
      ~EnvironmentInterface.get_env_var_option
      ~EnvironmentInterface.get_env_vars
      ~EnvironmentInterface.get_option_types
      ~EnvironmentInterface.install_project
      ~EnvironmentInterface.install_project_dev_mode
      ~EnvironmentInterface.join_command_args
      ~EnvironmentInterface.remove
      ~EnvironmentInterface.resolve_commands
      ~EnvironmentInterface.run_shell_command
      ~EnvironmentInterface.sync_dependencies
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~EnvironmentInterface.PLUGIN_NAME
      ~EnvironmentInterface.app
      ~EnvironmentInterface.builder
      ~EnvironmentInterface.config
      ~EnvironmentInterface.context
      ~EnvironmentInterface.data_directory
      ~EnvironmentInterface.dependencies
      ~EnvironmentInterface.dependencies_complex
      ~EnvironmentInterface.description
      ~EnvironmentInterface.dev_mode
      ~EnvironmentInterface.env_exclude
      ~EnvironmentInterface.env_include
      ~EnvironmentInterface.env_vars
      ~EnvironmentInterface.environment_dependencies
      ~EnvironmentInterface.environment_dependencies_complex
      ~EnvironmentInterface.features
      ~EnvironmentInterface.isolated_data_directory
      ~EnvironmentInterface.matrix_variables
      ~EnvironmentInterface.metadata
      ~EnvironmentInterface.name
      ~EnvironmentInterface.pathsep
      ~EnvironmentInterface.platform
      ~EnvironmentInterface.platforms
      ~EnvironmentInterface.post_install_commands
      ~EnvironmentInterface.pre_install_commands
      ~EnvironmentInterface.project_root
      ~EnvironmentInterface.root
      ~EnvironmentInterface.scripts
      ~EnvironmentInterface.sep
      ~EnvironmentInterface.skip_install
      ~EnvironmentInterface.system_python
      ~EnvironmentInterface.verbosity
   
   