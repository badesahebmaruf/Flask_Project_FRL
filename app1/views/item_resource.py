from flask_restful import Resource,reqparse
from app1.controllers.item_controller import ItemController
from flask import jsonify

class ItemResource(Resource):
    def get(self):
        return 'hello'
    
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True)
        parser.add_argument('quantity',type=int,required=True)
        request_body=parser.parse_args()
        
        name= request_body.get('name')
        quantity = request_body.get('quantity')
        res=ItemController.insert_data(name,quantity)
        print(res)
        return {'name':res.name ,'quantity':res.quantity}
    
    def get(self):
        items=ItemController.get_all_items()
        return {'items':[{'name':item.name,'quantity':item.quantity} for item in items]}

class ItemListResource(Resource):    
    def put(self,item_id):
        parser=reqparse.RequestParser()
        parser.add_argument('name',type=str,required=True)
        request_body=parser.parse_args()    
        
        item=ItemController.update_item(item_id,request_body['name'])
        if item:
            return {'name':item.name}
        return {'message':'item not found'},404
    
    def delete(self,item_id):
        item=ItemController.delete_item(item_id)
        if item:
            return {'message':'Item deleted'}
        return {'message':'item not found'},400
        
    def get(self,item_id):
        items=ItemController.get_item_by_id(item_id)
        if items:
            return {'name':items.name,'quantity':items.quantity}
        return jsonify('message','Item not found')    