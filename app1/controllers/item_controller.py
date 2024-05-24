from app1.models.item_model import ItemsModel
from app1 import db


class ItemController:
    @staticmethod
    def insert_data(name,quantity):
        new_item = ItemsModel(name=name , quantity =quantity)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    
    @staticmethod
    def update_item(item_id,name):
        item=db.session.get(ItemsModel,item_id)
        if item:
            item.name=name
            db.session.commit()
            return item
    
    @staticmethod
    def delete_item(item_id):
        item=db.session.get(ItemsModel,item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return item
    
    @staticmethod
    def get_all_items():
        return ItemsModel.query.all()
    
    @staticmethod
    def get_item_by_id(item_id):
        return ItemsModel.query.get(item_id)