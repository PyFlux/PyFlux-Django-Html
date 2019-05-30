class DashboardMenu():
    menu_items = [{
        "menu_text": "Control Panel",
        'menu_icon': '<i class="fa fa-tasks"></i>',
        'acl_key': 'dashboard.userpanel',
        'main_menu_key': 'control.panel',
        'level': '0',
        'sub_menu': [{
            'link': '#',
            'menu_text': 'User Management',
            'menu_icon': '<i class="fa fa-tasks"></i>',
            'acl_key': 'dashboard.usermanagement',
            'sub_menu_key': 'control.panel',
            'level': '1',
            'sub_sub_menu':
                [{

                    'link': '/admin/list/users',
                    'menu_text': 'Users',
                    'menu_icon': '<i class="fa fa-tasks"></i>',
                    'acl_key': 'dashboard.admin.users',
                    'sub_sub_menu_key': 'control.panel',
                    'level': '2',
                    'app_name': 'Dashboard',
                    'model_name': 'Users',

                },
                    {
                        'link': '/admin/list/roles',
                        'menu_text': 'Roles',
                        'menu_icon': '<i class="fa fa-tasks"></i>',
                        'acl_key': 'dashboard.admin.roles',
                        'sub_sub_menu_key': 'control.panel',
                        'level': '2',
                        'app_name': 'Dashboard',
                        'model_name': 'Roles',
                    },
                ]

        },

            {
                'link': '#',
                'menu_text': 'Assign User Roles',
                'menu_icon': '<i class="fa fa-tasks"></i>',
                'acl_key': 'dashboard.userroles',
                'sub_menu_key': 'control.panel',
                'level': '1',
                'sub_sub_menu':
                    [{

                        'link': '/admin/list/userroles',
                        'menu_text': 'User Roles',
                        'menu_icon': '<i class="fa fa-tasks"></i>',
                        'acl_key': 'dashboard.admin.userroles',
                        'sub_sub_menu_key': 'control.panel',
                        'level': '2',
                        'app_name': 'Dashboard',
                        'model_name': 'Userroles',

                    },
                    ]

            }

        ]
    },

        {
            "menu_text": "System Config",
            'menu_icon': '<i class="fa fa-cogs"></i>',
            'acl_key': 'dashboard.systemconfig',
            'main_menu_key': 'control.systemconfig',
            'level': '0',
            'sub_menu': [{
                'link': '#',
                'menu_text': 'Configuration',
                'menu_icon': '<i class="fa fa-tasks"></i>',
                'acl_key': 'dashboard.configuration',
                'sub_menu_key': 'control.systemconfig',
                'level': '1',
                'sub_sub_menu':
                    [{

                        'link': '/admin/list/country',
                        'menu_text': 'Country',
                        'menu_icon': '<i class="fa fa-tasks"></i>',
                        'acl_key': 'dashboard.admin.country',
                        'sub_sub_menu_key': 'control.systemconfig',
                        'level': '2',
                        'app_name': 'systemconfig',
                        'model_name': 'Country',

                    },
                        {

                            'link': '/admin/list/state',
                            'menu_text': 'State',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.state',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'State',

                        },

                        {

                            'link': '/admin/list/citytown',
                            'menu_text': 'City/Town',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.citytown',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'CityTown',

                        },

                        {

                            'link': '/admin/list/languages',
                            'menu_text': 'Language',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.languages',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Language',

                        },

                        {

                            'link': '/admin/list/nationality',
                            'menu_text': 'Nationality',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.nationality',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Nationality',

                        },
                        {

                            'link': '/admin/list/religion',
                            'menu_text': 'Religion',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.religion',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Religion',

                        },

                        {

                            'link': '/admin/list/relationship',
                            'menu_text': 'Relationship',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.relationship',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Relationship',

                        },
                        {

                            'link': '/admin/list/occupation',
                            'menu_text': 'Occupation',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.occupation',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Occupation',

                        },

                    ]

            },
                {
                    'link': '#',
                    'menu_text': 'Organization',
                    'menu_icon': '<i class="fa fa-tasks"></i>',
                    'acl_key': 'dashboard.organization',
                    'sub_menu_key': 'control.systemconfig',
                    'level': '1',
                    'sub_sub_menu':
                        [{

                            'link': '/admin/list/organization',
                            'menu_text': 'Organization',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.organization',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Organization',

                        },

                        ]

                },
                {
                    'link': '#',
                    'menu_text': 'Sms/Email',
                    'menu_icon': '<i class="fa fa-tasks"></i>',
                    'acl_key': 'dashboard.sms/email',
                    'sub_menu_key': 'control.systemconfig',
                    'level': '1',
                    'sub_sub_menu':
                        [{

                            'link': '/admin/list/smsconfig',
                            'menu_text': 'Sms Config',
                            'menu_icon': '<i class="fa fa-tasks"></i>',
                            'acl_key': 'dashboard.admin.smsconfig',
                            'sub_sub_menu_key': 'control.systemconfig',
                            'level': '2',
                            'app_name': 'systemconfig',
                            'model_name': 'Smsconfig',

                        },
                            {

                                'link': '/admin/list/emailconfig',
                                'menu_text': 'Email Config',
                                'menu_icon': '<i class="fa fa-tasks"></i>',
                                'acl_key': 'dashboard.admin.emailconfig',
                                'sub_sub_menu_key': 'control.systemconfig',
                                'level': '2',
                                'app_name': 'systemconfig',
                                'model_name': 'Emailconfig',

                            },

                        ]

                }]
        },

    ]
