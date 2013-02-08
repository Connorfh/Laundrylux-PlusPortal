from twilio import twiml
from twilio.rest import TwilioRestClient

# coding: utf8

'''
Use Cases:
- Add location with contact info, SMS number
- Send message to location (status = 'processed')
- Receive message from location (status - 'received')
- Edit message (e.g., mark as accepted, processed)
- Manage list of locations (with links to edit, send message, etc.)
- Manage list of messages (e.g., view new messages)
'''
    
@auth.requires_login()
def add_location():
    form=SQLFORM(db.t_plus_location)
    if form.process().accepted:
        session.flash = 'form accepted'
        #redirect(URL('viewlocations'))
    elif form.errors:
        response.flash = 'form has errors'
    #else:
    #    response.flash = 'please fill the form'
    return dict(form=form)
    
@auth.requires_login()
def manage_locations():
    grid=SQLFORM.smartgrid(db.t_plus_location,
        onupdate=auth.archive, 
        linked_tables=['t_plus_machine', 't_plus_sms_message'])
    func = request.function
    if (func == 'wiki'):
        return grid
    else:
        return dict(form=grid)

@auth.requires_login()
def manage_machines():
    grid=SQLFORM.smartgrid(db.t_plus_machine,
        onupdate=auth.archive)
    func = request.function
    if (func == 'wiki'):
        return grid
    else:
        return dict(form=grid)

@auth.requires_login()           
def manage_messages():
    grid=SQLFORM.smartgrid(db.t_plus_sms_message,
        linked_tables=['t_plus_location'])
    return grid
    
def receivesms():
    ''' receive sms message, insert into db, reply for confirmation '''
    # test with plusportal2/plusc/receivesms?From=15167217331&To=15162047575&Body=Hello
    
    db.t_plus_sms_message.insert(
        f_from = request.vars['From'],
        f_to = request.vars.To,
        f_body = request.vars.Body)
        
    #sender = request.vars['From'][-10:]+'@vtext.com'
    #mail.send([sender],'hello',request.vars.Body)
    
    resp = twiml.Response()
    # resp.sms("hello")
    
    return str(resp) # dict()
    
def chart():
    
    chartdata = (['Loc A', 3],
          ['Loc B', 1],
          ['Loc C', 4],
          ['Loc D', 1],
          ['Loc E', 2])
    #chartdata=chartdata, charttitle='Messages by Loc'
    return dict(charttitle='Messages by Loc')
