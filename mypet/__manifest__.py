{
    'name': "My pet - minhng.info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'sequence' : -100,
    'author': "minhng.info",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'sale',
    ],
    'data':
[

    'views/my_pet_views.xml',
    'security/ir.model.access.csv',
    'views/sale.xml',
],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
