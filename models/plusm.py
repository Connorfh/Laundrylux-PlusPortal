# coding: utf8

# t_plus_contact, t_plus_distributor, t_plus_location, t_plus_location_contact, t_plus_machine, t_plus_sms_message

########################################
db.define_table('t_plus_distributor',
    Field('f_name', type='string', label=T('Name')),
    Field('f_street', type='string', label=T('Street')),
    Field('f_street2', type='string', label=T('Street 2')),
    Field('f_city', type='string', label=T('City')),
    Field('f_state', type='string', label=T('State')),
    Field('f_zip', type='string', label=T('ZIP')),
    Field('f_contact_name', type='string', label=T('Contact Name')),
    Field('f_contact_phone', type='string', label=T('Contact Phone')),
    auth.signature,
    format='%(f_name)s',
    singular='Distributor', plural='Distributors',
    migrate=True)
    
########################################
db.define_table('t_plus_location',
    Field('f_name', type='string', label=T('Name')),
    Field('f_location_id', type='string', label=T('Location ID')),
    Field('f_street', type='string', label=T('Street')),
    Field('f_street2', type='string', label=T('Street 2')),
    Field('f_city', type='string', label=T('City')),
    Field('f_status', type='string', label=T('State')),
    Field('f_zip', type='string', label=T('ZIP')),
    Field('f_sms_phone_number', type='string', notnull=True, unique=True, label=T('SMS Phone Number')),
    Field('f_sms_provider', type='string', label=T('SMS Provider')),
    Field('f_contact_name', type='string', label=T('Contact Name')),
    Field('f_contact_phone', type='string', label=T('Contact Phone')),
    Field('f_four_week_point_level', type='integer', label=T('Four Week Point Level')),
    Field('f_distributor', type='reference t_plus_distributor', label=T('Distributor')),
    auth.signature,
    format='%(f_location_id)s - %(f_name)s',
    singular='Location', plural='Locations',
    migrate=True)

#db.define_table('t_plus_location_archive', db.t_plus_location, Field('current_record','reference t_plus_location',readable=False,writable=False))

########################################
db.define_table('t_plus_contact',
    Field('f_name', type='string', label=T('Name')),
    Field('f_street', type='string', label=T('Street')),
    Field('f_street2', type='string', label=T('Street 2')),
    Field('f_city', type='string', label=T('City')),
    Field('f_status', type='string', label=T('State')),
    Field('f_zip', type='string', label=T('ZIP')),
    Field('f_contact_name', type='string', label=T('Contact Name')),
    Field('f_sms_phone_number', type='string', notnull=True, unique=True, label=T('SMS Phone Number')),
    Field('f_sms_provider', type='string', label=T('SMS Provider')),
    auth.signature,
    format='%(f_name)s - %(f_contact_name)s',
    singular='Contact', plural='Contacts',
    migrate=True)
    
########################################
db.define_table('t_plus_location_contact',
    Field('f_contact', type='reference t_plus_contact', label=T('Contact')),
    Field('f_location', type='reference t_plus_location', label=T('Location')),
    Field('f_type', type='string', label=T('Type'), 
        requires=IS_IN_SET(['Owner 1', 'Owner 2', 'Owner 3', 'Operator 1', 'Operator 2', 'Operator 3', 'Service 1', 'Service 2', 'Service 3'],zero='')),
    auth.signature,
    format='%(f_contact)s',
    singular='Location Contact', plural='Location Contacts',
    migrate=True)
    
########################################
db.define_table('t_plus_machine',
    Field('f_number', type='string', label=T('Number')),
    Field('f_name', type='string', label=T('Name')),
    Field('f_location', type='reference t_plus_location', label=T('Location')),
    Field('f_serial_number', type='string', label=T('Serial Number')),
    auth.signature,
    format='%(f_name)s',
    singular='Machine', plural='Machines',
    migrate=True)

#db.define_table('t_plus_machine_archive', db.t_plus_machine, Field('current_record','reference t_plus_machine',readable=False,writable=False))

########################################
db.define_table('t_plus_sms_message',
    Field('f_from', type='string', label=T('From')),
    Field('f_to', type='string', label=T('To')),
    Field('f_body', type='string', label=T('Body')),
    Field('f_location', type='reference t_plus_location', label=T('Location')),
    Field('f_status', type='string', label=T('Status'), requires=IS_IN_SET(['New', 'Reviewed', 'Processed'],zero='')),
    Field('f_direction', type='string', label=T('Direction'), requires=IS_IN_SET(['Received', 'Sent'],zero='')),
    Field('f_points', type='integer', label=T('Points')),
    Field('f_sales_order_num', type='integer', label=T('Sales Order Number')),
    Field('f_parent_msg', type='reference t_plus_sms_message', label=T('Parent Message')),
    auth.signature,
    format='%(id)s - %(f_body)s',
    singular='SMS Message', plural='SMS Messages',
    migrate=True)
    
db.t_plus_sms_message.f_parent_msg.requires = IS_EMPTY_OR(IS_IN_DB(db, 't_plus_sms_message.id', '%(f_body)s'))
db.t_plus_sms_message.f_parent_msg.represent = (lambda value, row: ('%s %s' % (row.id, row.f_body)))

db.t_plus_location.f_sms_phone_number.requires = IS_NOT_EMPTY()
db.t_plus_location.f_sms_phone_number.requires = IS_NOT_IN_DB(db, db.t_plus_location.f_sms_phone_number)

db.t_plus_machine.f_location.requires = IS_IN_DB(db, db.t_plus_location.id, '%(f_name)s')
db.t_plus_machine.f_location.represent = (lambda value, row: A(row.f_location.f_name, _href=URL('plus_location_manage', args=['t_plus_location', 'view', 't_plus_location', row.f_location.id], user_signature=True)))

db.t_plus_sms_message.created_on.readable = db.t_plus_sms_message.created_by.readable = True
#db.t_plus_sms_message.created_on.writable = db.t_plus_sms_message.created_by.writable = False

#shift=datetime.timedelta(....) 
#db.table.field.represent = lambda d,r,s=shift: prettydate(d+s)
