# coding: utf-8

"""
    CDO API

    Use the documentation to explore the endpoints CDO has to offer

    The version of the OpenAPI document: 1.4.0
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cdo_sdk_python.models.redirect_view import RedirectView

class TestRedirectView(unittest.TestCase):
    """RedirectView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RedirectView:
        """Test RedirectView
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RedirectView`
        """
        model = RedirectView()
        if include_optional:
            return RedirectView(
                application_context = cdo_sdk_python.models.application_context.ApplicationContext(
                    parent = cdo_sdk_python.models.application_context.ApplicationContext(
                        id = '', 
                        display_name = '', 
                        autowire_capable_bean_factory = cdo_sdk_python.models.autowire_capable_bean_factory.autowireCapableBeanFactory(), 
                        application_name = '', 
                        startup_date = 56, 
                        environment = cdo_sdk_python.models.environment.Environment(
                            active_profiles = [
                                ''
                                ], 
                            default_profiles = [
                                ''
                                ], ), 
                        bean_definition_count = 56, 
                        bean_definition_names = [
                            ''
                            ], 
                        parent_bean_factory = cdo_sdk_python.models.parent_bean_factory.parentBeanFactory(), 
                        class_loader = cdo_sdk_python.models.application_context_class_loader.ApplicationContext_classLoader(
                            name = '', 
                            registered_as_parallel_capable = True, 
                            unnamed_module = cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module.ApplicationContext_classLoader_parent_unnamedModule(
                                name = '', 
                                descriptor = cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module_descriptor.ApplicationContext_classLoader_parent_unnamedModule_descriptor(
                                    open = True, 
                                    automatic = True, ), 
                                named = True, 
                                annotations = [
                                    None
                                    ], 
                                declared_annotations = [
                                    None
                                    ], 
                                packages = [
                                    ''
                                    ], 
                                layer = cdo_sdk_python.models.layer.layer(), ), 
                            defined_packages = [
                                cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module_class_loader_defined_packages_inner.ApplicationContext_classLoader_parent_unnamedModule_classLoader_definedPackages_inner(
                                    name = '', 
                                    sealed = True, 
                                    specification_title = '', 
                                    specification_version = '', 
                                    specification_vendor = '', 
                                    implementation_title = '', 
                                    implementation_version = '', 
                                    implementation_vendor = '', )
                                ], 
                            default_assertion_status = True, ), ), 
                    id = '', 
                    display_name = '', 
                    autowire_capable_bean_factory = cdo_sdk_python.models.autowire_capable_bean_factory.autowireCapableBeanFactory(), 
                    application_name = '', 
                    startup_date = 56, 
                    environment = cdo_sdk_python.models.environment.Environment(), 
                    bean_definition_count = 56, 
                    bean_definition_names = [
                        ''
                        ], 
                    parent_bean_factory = cdo_sdk_python.models.parent_bean_factory.parentBeanFactory(), 
                    class_loader = cdo_sdk_python.models.application_context_class_loader.ApplicationContext_classLoader(
                        name = '', 
                        registered_as_parallel_capable = True, 
                        default_assertion_status = True, ), ),
                servlet_context = cdo_sdk_python.models.redirect_view_servlet_context.RedirectView_servletContext(
                    session_timeout = 56, 
                    class_loader = cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module_class_loader.ApplicationContext_classLoader_parent_unnamedModule_classLoader(
                        name = '', 
                        registered_as_parallel_capable = True, 
                        defined_packages = [
                            cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module_class_loader_defined_packages_inner.ApplicationContext_classLoader_parent_unnamedModule_classLoader_definedPackages_inner(
                                name = '', 
                                annotations = [
                                    None
                                    ], 
                                declared_annotations = [
                                    None
                                    ], 
                                sealed = True, 
                                specification_title = '', 
                                specification_version = '', 
                                specification_vendor = '', 
                                implementation_title = '', 
                                implementation_version = '', 
                                implementation_vendor = '', )
                            ], 
                        default_assertion_status = True, ), 
                    major_version = 56, 
                    minor_version = 56, 
                    attribute_names = cdo_sdk_python.models.attribute_names.attributeNames(), 
                    context_path = '', 
                    init_parameter_names = cdo_sdk_python.models.init_parameter_names.initParameterNames(), 
                    session_tracking_modes = [
                        'COOKIE'
                        ], 
                    servlet_names = cdo_sdk_python.models.servlet_names.servletNames(), 
                    default_session_tracking_modes = [
                        'COOKIE'
                        ], 
                    effective_session_tracking_modes = [
                        'COOKIE'
                        ], 
                    jsp_config_descriptor = cdo_sdk_python.models.redirect_view_servlet_context_jsp_config_descriptor.RedirectView_servletContext_jspConfigDescriptor(
                        taglibs = [
                            cdo_sdk_python.models.redirect_view_servlet_context_jsp_config_descriptor_taglibs_inner.RedirectView_servletContext_jspConfigDescriptor_taglibs_inner(
                                taglib_uri = '', 
                                taglib_location = '', )
                            ], 
                        jsp_property_groups = [
                            cdo_sdk_python.models.redirect_view_servlet_context_jsp_config_descriptor_jsp_property_groups_inner.RedirectView_servletContext_jspConfigDescriptor_jspPropertyGroups_inner(
                                el_ignored = '', 
                                scripting_invalid = '', 
                                page_encoding = '', 
                                is_xml = '', 
                                include_preludes = [
                                    ''
                                    ], 
                                include_codas = [
                                    ''
                                    ], 
                                deferred_syntax_allowed_as_literal = '', 
                                trim_directive_whitespaces = '', 
                                error_on_undeclared_namespace = '', 
                                buffer = '', 
                                default_content_type = '', 
                                url_patterns = [
                                    ''
                                    ], )
                            ], ), 
                    virtual_server_name = '', 
                    request_character_encoding = '', 
                    response_character_encoding = '', 
                    effective_major_version = 56, 
                    effective_minor_version = 56, 
                    servlets = cdo_sdk_python.models.servlets.servlets(), 
                    server_info = '', 
                    servlet_context_name = '', 
                    servlet_registrations = {
                        'key' : cdo_sdk_python.models.redirect_view_servlet_context_servlet_registrations_value.RedirectView_servletContext_servletRegistrations_value(
                            mappings = [
                                ''
                                ], 
                            run_as_role = '', 
                            name = '', 
                            class_name = '', 
                            init_parameters = {
                                'key' : ''
                                }, )
                        }, 
                    filter_registrations = {
                        'key' : cdo_sdk_python.models.redirect_view_servlet_context_filter_registrations_value.RedirectView_servletContext_filterRegistrations_value(
                            servlet_name_mappings = [
                                ''
                                ], 
                            url_pattern_mappings = [
                                ''
                                ], 
                            name = '', 
                            class_name = '', )
                        }, 
                    session_cookie_config = cdo_sdk_python.models.redirect_view_servlet_context_session_cookie_config.RedirectView_servletContext_sessionCookieConfig(
                        http_only = True, 
                        name = '', 
                        path = '', 
                        comment = '', 
                        secure = True, 
                        domain = '', 
                        max_age = 56, ), ),
                content_type = '',
                request_context_attribute = '',
                static_attributes = {
                    'key' : None
                    },
                expose_path_variables = True,
                expose_context_beans_as_attributes = True,
                exposed_context_bean_names = [
                    ''
                    ],
                bean_name = '',
                url = '',
                context_relative = True,
                http10_compatible = True,
                expose_model_attributes = True,
                encoding_scheme = '',
                status_code = '100 CONTINUE',
                expand_uri_template_variables = True,
                propagate_query_params = True,
                hosts = [
                    ''
                    ],
                redirect_view = True,
                propagate_query_properties = True,
                attributes_map = {
                    'key' : None
                    },
                attributes_csv = '',
                attributes = {
                    'key' : ''
                    }
            )
        else:
            return RedirectView(
        )
        """

    def testRedirectView(self):
        """Test RedirectView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
