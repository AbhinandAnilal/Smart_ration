from flask import *
from database import *

shop=Blueprint("shop",__name__)
@shop.route('/shophome')
def shophome():
	return render_template('shophome.html')


@shop.route('/shop_producttype')
def shop_producttype():
	data={}
	r="select * from type"
	data['view']=select(r)
	return render_template('shop_view_productby_type.html',data=data)



@shop.route('/shop_productbytype')
def shop_productbytype():
	data={}
	type_id=request.args['type_id']
	r="select * from setproducttotype inner join products using(product_id)  where type_id='%s'"%(type_id)
	data['view']=select(r)
	return render_template('shop_view_product.html',data=data)

@shop.route('/shop_view_stock',methods=['get','post'])
def shop_view_stock():
	data={}
	if 'submit' in request.form:
		pro_id=request.form['pro_id']
		kiloorlitter=request.form['kiloorlitter']
		u="insert into stock values(null,'%s',curdate())"%(session['shop_id'])
		res=insert(u)
		uu="insert into stockdetail values(null,'%s','%s','%s')"%(res,pro_id,kiloorlitter)
		insert(uu)
	if 'action' in request.args:
		action=request.args['action']
		detail_id=request.args['detail_id']
	else:
		action=None
	if action=='update':
		r="select * from stockdetail where detail_id='%s'"%(detail_id)
		data['up']=select(r)
	if 'update' in request.form:
		pro_id=request.form['pro_id']
		kiloorlitter=request.form['kiloorlitter']
		i="update stockdetail set product_id='%s',kiloorlitter='%s' where detail_id='%s'"%(pro_id,kiloorlitter,detail_id)
		update(i)
	if action=='delete':
		r="delete from stockdetail where detail_id='%s'"%(detail_id)
		delete(r)
	uu="select * from products"
	data['pro']=select(uu)
	r="select * from stock inner join stockdetail using(stock_id) INNER JOIN products USING(product_id) where shop_id='%s'"%(session['shop_id'])
	data['view']=select(r)
	return render_template('shop_add_stock.html',data=data)
@shop.route('/shop_view_timeslot')
def shop_view_timeslot():
	data={}
	
	r="select * from timeallocate inner join users using(user_id) where shop_id='%s'"%(session['shop_id'])
	data['view']=select(r)
	if 'action' in request.args:
		action=request.args['action']
		time_id=request.args['time_id']
	else:
		action=None
	if action=='accept':
		u="update timeallocate set status='Accept' where time_id='%s'"%(time_id)
		update(u)
		return redirect(url_for('shop.shop_view_timeslot'))
	if action=='reject':
		u="update timeallocate set status='Reject' where time_id='%s'"%(time_id)
		update(u)
		return redirect(url_for('shop.shop_view_timeslot'))


	return render_template('shop_view_timeslot.html',data=data)

@shop.route('/shop_view_rating')
def shop_view_rating():
	data={}
	
	r="select * from rating inner join users using(user_id)  where shop_id='%s'"%(session['shop_id'])
	data['view']=select(r)
	return render_template('shop_view_rating.html',data=data)

@shop.route('/search_by_rationcard',methods=['get','post'])
def search_by_rationcard():
	data={}
	if 'search' in request.form:
		search=request.form['search']
		r="select * from rationcard where cardnumber like '%s'"%(search)
		data['view']=select(r)
	else:
		r="select * from rationcard inner join users"
		data['view']=select(r)
	
	
	return render_template('search_by_rationcard.html',data=data)
@shop.route('/view_product',methods=['get','post'])
def view_product():
	data={}
	type_id=request.args['type_id']

	r="select * from products inner join setproducttotype using(product_id) where type_id='%s'"%(type_id)
	data['view']=select(r)
	
	
	return render_template('shop_view_product.html',data=data)