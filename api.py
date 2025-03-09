from flask import *
from database import *
import uuid

api=Blueprint("api",__name__)





@api.route('/userhome',methods=['get','post'])
def	userhome():
    data={}
    idd=session['uid']
    data['uid']=idd
    return render_template('user_home.html',data=data)


@api.route('/user_send_request',methods=['post','GET'])
def user_send_request():
	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='request':


		hj="insert into requestrationcard values(null,'%s','pending')"%(session['uid'])
		res=insert(hj)
		flash("Request send successfully")
		return redirect(url_for('api.userhome'))


@api.route('/user_view_request',methods=['post','GET'])
def user_view_request():
	data={}

	kk="select * from requestrationcard inner join users using(user_id) where user_id='%s'"%(session['uid'])
	data['view']=select(kk)
	
	return render_template('user_view_request.html',data=data)





@api.route('/user_view_card_details',methods=['post','GET'])
def user_view_card_details():
	data={}
	request_idd=request.args['request_idd']
	hj="SELECT * FROM `rationcard`INNER JOIN `type`USING(`type_id`)WHERE `request_id`='%s'"%(request_idd)
	data['view']=select(hj)
	return render_template('user_view_card_details.html',data=data)

@api.route('/user_view_Notification',methods=['post','GET'])
def user_view_Notification():
	data={}
	hj="SELECT * FROM `notification` "
	data['view']=select(hj)
	return render_template('user_view_Notification.html',data=data)



@api.route('/user_send_feedback',methods=['post','GET'])
def user_send_feedback():
	data={}
	if 'submit' in request.form:
		feedback=request.form['feedback']
		
		gf="insert into feedback values(null,'%s','%s',curdate())"%(session['uid'],feedback)
		res=insert(gf)
		flash("Feedback send successfully")
	hj="SELECT * FROM `feedback`where user_id='%s'"%(session['uid'])
	data['view']=select(hj)
	return render_template('user_send_feedback.html',data=data)

@api.route('/user_view_feedback',methods=['post'])
def user_view_feedback():
	data={}
	lid=request.form['lid']
	hj="SELECT * FROM `feedback`where user_id=(SELECT user_id FROM `users`WHERE `login_id`='%s')"%(lid)
	res=select(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@api.route('/user_view_shopkeeper',methods=['post','GET'])
def user_view_shopkeeper():
	data={}
	hj="SELECT * FROM `shop`"
	data['view']=select(hj)
	return render_template('user_view_shopkeeper.html',data=data)


@api.route('/user_send_Rating',methods=['get','post'])
def user_send_Rating():
	data={}
	if 'submit' in request.form:
		shop_idd=request.args['r_id']
		rating=request.form['rating']
		q="insert into rating values(NULL,'%s','%s','%s',curdate())"%(shop_idd,session['uid'],rating)
		id=insert(q)
		flash("Rating send successfully")
		return redirect(url_for('api.userhome'))
	shop_idd=request.args['r_id']
	q="select * from rating where shop_id='%s' and user_id='%s'"%(shop_idd,session['uid'])
	data['view']=select(q)
	return render_template('user_send_Rating.html',data=data)


@api.route('/user_view_review_comapny',methods=['get','post'])
def user_view_review_comapny():
	data={}
	shop_idd=request.args['shop_idd']
	login_id=request.args['loginid']
	q="select * from rating where shop_id='%s' and user_id=(select user_id from users where login_id='%s')"%(shop_idd,login_id)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']='user_view_review_comapny'
	return  demjson.encode(data)


@api.route('/user_send_time_scheduling',methods=['post','GET'])
def user_send_time_scheduling():
	data={}
	if 'submit' in request.form:
		t_time=request.form['t_time']
		d_date=request.form['d_date'] 
		shop_id=request.args['r_id'] 
		
		gf="insert into timeallocate values(null,'%s','%s','%s','%s','pending')"%(session['uid'],shop_id,d_date,t_time)
		res=insert(gf)
	shop_id=request.args['r_id'] 
	hj="SELECT * FROM `timeallocate` where user_id='%s' and shop_id='%s'"%(session['uid'],shop_id)
	data['view']=select(hj)
	return render_template('user_send_time_scheduling.html',data=data)


@api.route('/user_view_time_request',methods=['post'])
def user_view_time_request():
	data={}
	lid=request.form['lid']
	shop_id=request.form['shop_id']
	hj="SELECT * FROM `timeallocate` where user_id=(SELECT user_id FROM `users`WHERE `login_id`='%s') and shop_id='%s'"%(lid,shop_id)
	res=select(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")






@api.route('/user_view_my_items',methods=['post','GET'])
def user_view_my_items():
	data={}
	

	hj="SELECT * FROM `setproducttotype`INNER JOIN `type`USING(`type_id`)INNER JOIN `products`USING(`product_id`)INNER JOIN `rationcard`USING(`type_id`)INNER JOIN `requestrationcard`USING(`request_id`) where user_id='%s'"%(session['uid'])
	data['view']=select(hj)
	return render_template('user_view_my_items.html',data=data)


@api.route('/user_buy_product',methods=['post'])
def user_buy_product():
	lid=request.form['lid']
	
	
	return redirect('url_for("api.user_payment")')


@api.route('/user_view_buy_items',methods=['post','Get'])
def user_view_buy_items():
	data={}
	

	hj="SELECT * FROM `buydetails`INNER JOIN `buy`USING(`buy_id`)INNER JOIN `products`USING(`product_id`) inner join setproducttotype using(product_id) where user_id='%s'"%(session['uid'])
	data['view']=select(hj)
	return render_template('user_view_buy_items.html',data=data)



@api.route('/user_payment', methods=['post','GET'])
def user_payment():
	data={}
	aamount = request.args['aamount']
	data['amount']=aamount
	product_idd=request.args['product_idd']
	data['pid']=product_idd
	if 'submit' in request.form:
		aamount = request.form['amount']
		
		product_idd=request.form['product_idd']
		gf="insert into buy values(null,'%s','%s',curdate())"%(session['uid'],aamount)
		res1=insert(gf)
		gg="insert into buydetails values(null,'%s','%s','1','%s','pending')"%(res1,product_idd,aamount)
		res=insert(gg)
		gf = "insert into payment values(null,'%s','%s',curdate())" % (res,aamount)
		res = insert(gf)
		flash("Payment Successfull")
		return redirect(url_for('api.userhome'))
	return render_template('user_payment.html',data=data)


@api.route('/user_view_payment',methods=['post'])
def user_view_payment():
	buy_idd=request.form['buy_idd']
	hj="SELECT * FROM `payment` where buy_id='%s'"%(buy_idd)
	res=select(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")




@api.route('/user_address',methods=['post'])
def user_address():
	lid=request.form['lid']
	addd=request.form['addd']
	pinn=request.form['pinn']
	placee=request.form['placee']
	phone=request.form['phone']
	gf="insert into delivery values(null,(SELECT user_id FROM `users`WHERE `login_id`='%s'),'%s','%s','%s','%s')"%(lid,addd,pinn,placee,phone)
	res=insert(gf)
	if res:
		return jsonify(status="ok")
	else:
		return jsonify(status="failed")