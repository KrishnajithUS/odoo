
{
    'name': 'Real Estate',
    'version': '1.2',
    'category': 'Custom/RealEstate',
    'sequence': 15,
    'summary': 'Test module for real estate',
    'description': "",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/real_estate_menu.xml',
        'views/real_estate.xml',
    ],
    'demo': [    ],
    'installable': True,
    'application': True,
    'auto_install': False
}