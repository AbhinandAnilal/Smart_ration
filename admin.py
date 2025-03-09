from flask import *
from database import *

admin=Blueprint("admin",__name__)
@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')
@admin.route('/rat_type',methods=['get','post'])
def rat_type():
	data={}
	if 'submit' in request.form:
		rat_type=request.form['rat_type']
		Details=request.form['Details']
		u="insert into type values(null,'%s','%s')"%(rat_type,Details)
		insert(u)
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if action=='update':
		y="select * from type where type_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		rat_type=request.form['rat_type']
		Details=request.form['Details']
		uu="update type set type='%s',details='%s' where type_id='%s'"%(rat_type,Details,r_id)
		update(uu)
	if action=='delete':
		r="delete from type where type_id='%s'"%(r_id)
		delete(r)
	r1="select* from type"
	data['view']=select(r1)
	return render_template('admin_ration_type.html',data=data)
@admin.route('/gov_staff',methods=['get','post'])
def gov_staff():
	data={}
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		designation=request.form['designation']
		uname=request.form['uname']
		password=request.form['pwd']
		y3="insert into login values(null,'%s','%s','govtstaff')"%(uname,password)
		log=insert(y3)
		u="insert into govtstaff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(log,fname,lname,place,phone,email,designation)
		insert(u)
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if action=='update':
		y="select * from govtstaff where staff_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		designation=request.form['designation']
		uu="update govtstaff set fname='%s',lname='%s',place='%s',phone='%s',email='%s',designation='%s' where staff_id='%s'"%(fname,lname,place,phone,email,designation,r_id)
		update(uu)
	if action=='delete':
		r="delete from govtstaff where staff_id='%s'"%(r_id)
		delete(r)
	r1="select* from govtstaff"
	data['view']=select(r1)
	return render_template('admin_govt_staff.html',data=data)
@admin.route('/admin_add_product',methods=['get','post'])
def admin_add_product():
	data={}
	if 'submit' in request.form:
		product=request.form['product']
		Details=request.form['Details']
		amount=request.form['amount']
		

		u="insert into products values(null,'%s','%s','%s')"%(product,Details,amount)
		insert(u)
	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if action=='update':
		y="select * from products where product_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		product=request.form['product']
		Details=request.form['Details']
		amount=request.form['amount']
	
		uu="update products set product='%s',details='%s',amount='%s' where product_id='%s'"%(product,Details,amount,r_id)
		update(uu)
	if action=='delete':
		r="delete from products where product_id='%s'"%(r_id)
		delete(r)
	r1="select* from products"
	data['view']=select(r1)
	return render_template('admin_manage_product.html',data=data)
@admin.route('/admin_view_ration_request')
def admin_view_ration_request():
	data={}
	t="select *,users.designation as user_designation from requestrationcard inner join requestdetail using(request_id) inner join users using(user_id) where requestrationcard.status='upload' "
	data['view']=select(t)
	return render_template('admin_request_ration_card.html',data=data)
@admin.route('/admin_view_govstaff_details')
def admin_view_govstaff_details():
	data={}
	r_id=request.args['r_id']
	t="select * from staffdetail where request_id='%s'"%(r_id)
	data['view']=select(t)
	return render_template('admin_view_govstaff_details.html',data=data)
@admin.route('/admin_viewfeedback')
def admin_viewfeedback():
	data={}
	
	t="select * from feedback inner join users using(user_id)"
	data['view']=select(t)
	return render_template('admin_viewfeedback.html',data=data)
@admin.route('/admin_add_rationcard',methods=['get','post'])
def admin_add_rationcard():
	data={}

	if 'submit' in request.form:
		req_id=request.args['requset_id']
		card_number=request.form['card_number']
		type_id=request.form['type_id']
		

		u="insert into rationcard values(null,'%s','%s','%s',curdate())"%(card_number,req_id,type_id)
		insert(u)
		uu="update staffdetail set status='ration card' where request_id='%s'"%(req_id)
		update(uu)

	if 'action' in request.args:
		action=request.args['action']
		r_id=request.args['r_id']
	else:
		action=None
	if action=='update':
		y="select * from rationcard where rationcard_id='%s'"%(r_id)
		data['up']=select(y)
	if 'update' in request.form:
		card_number=request.form['card_number']
		type_id=request.form['type_id']
		
	
		uu="update rationcard set cardnumber='%s',type_id='%s' where rationcard_id='%s'"%(card_number,type_id,r_id)
		update(uu)
		return redirect(url_for('admin.adminhome'))
	if action=='delete':
		r="delete from rationcard where rationcard_id='%s'"%(r_id)
		delete(r)
		return redirect(url_for('admin.adminhome'))
	req_id=request.args['requset_id']
	r1="select* from rationcard inner join type using(type_id) where request_id='%s'"%(req_id)
	data['view']=select(r1)
	rr="select * from type"
	data['type']=select(rr)
	return render_template('generate_ration_card.html',data=data)