from odoo import api, fields, models  # type:ignore


class BookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _parent_store = True

    name = fields.Char(translate=True, required=True)
    highlighted_id = fields.Reference(
        [("library.book", "Book"), ("res.partner", "Author")],
        "Category Highlight",)
    
    # Hierarchy fields
    parent_id = fields.Many2one(
        "library.book.category",
        "Parent Category",
        ondelete="restrict")
    parent_path = fields.Char(index=True)
    
    # Optional, but nice to have:
    child_ids = fields.One2many(
        "library.book.category",
        "parent_id",
        "Subcategories")
