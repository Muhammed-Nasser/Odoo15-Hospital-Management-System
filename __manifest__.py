{
    'name': 'Hospital Management System',
    'version': '1.0.0',
    'sequence': '1',
    'summary': 'Hospital Management System',
    'description': 'Hospital Management System',
    'category': '',
    'author': 'Muhammad Nasser',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base',
                'mail',
                ],
    'data': [
        # menu should list after all views to read ids of actions
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False
}
