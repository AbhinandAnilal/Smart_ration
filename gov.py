from flask import *

from database import *

gov=Blueprint("gov",__name__)
@gov.route('/govhome')
def govhome():
	return render_template('govhome.html')
@gov.route('/gov_view_request')
def gov_view_request():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if action=='accept':
		t="update requestrationcard set status='accept' where request_id='%s'"%(r_id)
		update(t)
		return redirect(url_for('gov.gov_view_request'))
	if action=='reject':
		t="update requestrationcard set status='reject' where request_id='%s'"%(r_id)
		update(t)
		return redirect(url_for('gov.gov_view_request'))
	if action=='upload':
		t="update requestrationcard set status='upload' where request_id='%s'"%(r_id)
		update(t)
		return redirect(url_for('gov.gov_view_request'))
	t="select * from requestrationcard inner join users using(user_id)"
	data['view']=select(t)
	return render_template('gov_view_request.html',data=data)

@gov.route('/gov_add_details',methods=['get','post'])
def gov_add_details():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if 'submit' in request.form:
		r_id=request.args['r_id']
		name=request.form['name']
		relation=request.form['relation']
		designation=request.form['designation']
		i="insert into requestdetail values(null,'%s','%s','%s','%s')"%(r_id,name,relation,designation)
		insert(i)
	
	if action=='update':
		y="select * from requestdetail where rdetail_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		r_id=request.args['r_id']
		name=request.form['name']
		relation=request.form['relation']
		designation=request.form['designation']
		uu="update requestdetail set name='%s',relation='%s',designation='%s' where rdetail_id='%s'"%(name,relation,designation,r_id)
		update(uu)
	if action=='delete':
		r="delete from requestdetail where rdetail_id='%s'"%(r_id)
		delete(r)
	
	r_id=request.args['r_id']
	t="select * from requestdetail where request_id='%s'"%(r_id)
	data['view']=select(t)
	return render_template('gov_add_details.html',data=data)
@gov.route('/gov_view_product')
def gov_view_product():
	data={}
	
	t="select * from products"
	data['view']=select(t)
	return render_template('gov_view_product.html',data=data)
@gov.route('/gov_add_producttype',methods=['get','post'])
def gov_add_producttype():
	data={}
	
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if 'submit' in request.form:
		pro_id=request.args['pro_id']
		kiloorlitter=request.form['kiloorlitter']
		type1=request.form['type']
		forthemonth=request.form['forthemonth']
		i="insert into setproducttotype values(null,'%s','%s','%s','%s')"%(type1,pro_id,kiloorlitter,forthemonth)
		insert(i)
	
	if action=='update':
		y="select * from setproducttotype where ptype_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		r_id=request.args['r_id']
		kiloorlitter=request.form['kiloorlitter']
		type1=request.form['type']
		forthemonth=request.form['forthemonth']
		uu="update setproducttotype set type_id='%s',kiloorlitter='%s',forthemonth='%s' where ptype_id='%s'"%(type1,kiloorlitter,forthemonth,r_id)
		update(uu)
		return(redirect(url_for('gov.govhome')))
	if action=='delete':
		r="delete from setproducttotype where ptype_id='%s'"%(r_id)
		delete(r)
		return(redirect(url_for('gov.govhome')))
	rr="select * from type"
	data['type']=select(rr)
	pro_id=request.args['pro_id']
	t="select * from setproducttotype inner join type using(type_id) where product_id='%s'"%(pro_id)
	data['view']=select(t)
	return render_template('gov_product_type.html',data=data)
@gov.route('/gov_view_shop')
def gov_view_shop():
	data={}
	
	t="select * from shop"
	data['view']=select(t)
	return render_template('gov_view_shopkeeper.html',data=data)

@gov.route('/gov_stock_details')
def gov_stock_details():
	data={}
	
	t="select * from stock inner join stockdetail using(stock_id) inner join products using(product_id)"
	data['view']=select(t)
	return render_template('gov_stock_details.html',data=data)

@gov.route('/send_noti',methods=['get','post'])
def send_noti():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if 'submit' in request.form:
		
		name=request.form['notification']
		Details=request.form['Details']
		
		i="insert into notification values(null,'%s','%s',curdate())"%(name,Details)
		insert(i)
	
	if action=='update':
		y="select * from notification where notification_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		name=request.form['notification']
		Details=request.form['Details']
		uu="update notification set notification='%s',details='%s' where notification_id='%s'"%(name,Details,r_id)
		update(uu)
	if action=='delete':
		r="delete from notification where notification_id='%s'"%(r_id)
		delete(r)
	
	
	t="select * from notification"
	data['view']=select(t)
	return render_template('gov_send_notification.html',data=data)