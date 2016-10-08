# coding: utf-8

{
    'name': 'Tu portal web',
    'summary': '''
    Vendedor web
    ''',
    # Autoloaded on v9.0 from README.rst
    # 'description': '''
    'author': 'Tecno',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Installer',
    'version': '0.1',
    'depends': [
        'website_blog',
        'website_event_sale',
        'website_event_track',  # To manage webinars (silenced)
        'website_event_questions',
        'website_slides',
        'website_google_map',
        'website_crm',  # To have a contact form.
        'website_links',  # To track the marketing.
        'theme_clean',  # Vauxoo Theme will be just an extension
    ],
    'test': [
    ],
    'data': [
        'views/assets.xml',
        'views/home.xml',
    ],
    'demo': [
    ],
}
