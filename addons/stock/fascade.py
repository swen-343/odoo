import sys
sys.path.append('../../')
import openerp
from openerp import api
from openerp.modules.registry import RegistryManager


class Fascade():
    def __init__(self):
        self.registry = RegistryManager.get("inventorymanagement")
        #: current transaction's cursor
        self.cr = self.registry.cursor()
        self.uid = openerp.SUPERUSER_ID
        #: :class:`~openerp.api.Environment` for the current test case
        self.env = api.Environment(self.cr, self.uid, {})
        super(Requests, self).setUp()
        self.ProductObj = self.env['product.product']
        self.UomObj = self.env['product.uom']
        self.PartnerObj = self.env['res.partner']
        self.ModelDataObj = self.env['ir.model.data']
        self.StockPackObj = self.env['stock.pack.operation']
        self.StockQuantObj = self.env['stock.quant']
        self.PickingObj = self.env['stock.picking']
        self.MoveObj = self.env['stock.move']
        self.InvObj = self.env['stock.inventory']
        self.InvLineObj = self.env['stock.inventory.line']
        self.LotObj = self.env['stock.production.lot']
        self.stock_location = self.ModelDataObj.xmlid_to_res_id('stock.stock_location_stock')
        
    def modify_quantity(self, id, diff):
        if self.get_quantity(id)+diff<0:
            return False
        Wiz = self.env['stock.change.product.qty']
        wiz = Wiz.create({'product_id': id,
                          'new_quantity': self.get_quantity(id)+diff,
                          'location_id':  self.stock_location,
                          })
        wiz.change_product_qty()
        return True
    
    def get_quantity(self,product_id):
        context = {}
        qty_wh = 0;
        qty = self.ProductObj.get('product.product')._product_available(self.cr, self.uid, [product_id], context=dict(context or {}, location=stock_location))
        if product_id in qty:
            qty_wh = qty[product_id]['qty_available']
        return qty_wh
        
        
        
    
    