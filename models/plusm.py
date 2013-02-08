# coding: utf8

#todo add code to test compatibiity with mysql

########################################
db.define_table('t_plus_location',
    Field('f_name', type='string', label=T('Name')),
    Field('f_contact_name', type='string', label=T('Contact Name')),
    Field('f_sms_phone_number', type='string', notnull=True, unique=True, label=T('SMS Phone Number')),
    Field('f_sms_provider', type='string', label=T('SMS Provider')),
    auth.signature,
    format='%(f_name)s',
    singular='Location', plural='Locations',
    migrate=True)

db.define_table('t_plus_location_archive', db.t_plus_location, Field('current_record','reference t_plus_location',readable=False,writable=False))

########################################
db.define_table('t_plus_machine',
    Field('f_name', type='string', label=T('Name')),
    Field('f_location', type='reference t_plus_location', label=T('Location')),
    Field('f_serial_number', type='string', label=T('Serial Number')),
    auth.signature,
    format='%(f_name)s',
    singular='Machine', plural='Machines',
    migrate=True)

db.define_table('t_plus_machine_archive', db.t_plus_machine, Field('current_record','reference t_plus_machine',readable=False,writable=False))

########################################
db.define_table('t_plus_sms_message',
    Field('f_from', type='string', label=T('From')),
    Field('f_to', type='string', label=T('To')),
    Field('f_body', type='string', label=T('Body')),
    Field('f_location', type='reference t_plus_location', label=T('Location')),
    #todo add field for status (new, reviewed, processed)
    #todo add field for inbound/outbound (or sent/recieved)
    auth.signature,
    format='%(f_name)s',
    singular='SMS Message', plural='SMS Messages',
    migrate=True)

db.t_plus_location.f_sms_phone_number.requires = IS_NOT_EMPTY()
db.t_plus_location.f_sms_phone_number.requires = IS_NOT_IN_DB(db, db.t_plus_location.f_sms_phone_number)

db.t_plus_machine.f_location.requires = IS_IN_DB(db, db.t_plus_location.id, '%(title)s')
db.t_plus_machine.f_location.represent = (lambda value, row: A(row.f_location.f_name, _href=URL('plus_location_manage', args=['t_plus_location', 'view', 't_plus_location', row.f_location.id], user_signature=True)))

db.t_plus_sms_message.created_on.readable = db.t_plus_sms_message.created_by.readable = True

#shift=datetime.timedelta(....) 
#db.table.field.represent = lambda d,r,s=shift: prettydate(d+s)
