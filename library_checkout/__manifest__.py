{ "name": "Library Book Checkout",
  "description": "Members can borrow books from the library.",
  "author": "Daniel Reis",
  "depends": ["library_member", "mail"],
  "data": [
    "security/ir.model.access.csv",
    "views/library_menu.xml",
    "views/checkout_view.xml",
    "views/checkout_kanban_view.xml",
    "wizard/checkout_mass_message_wizard_view.xml",
    "data/library_checkout_stage.xml",
  ],
  "assets": {
        "web.assets_backend": {
            "library_checkout/static/src/css/checkout.css",
            "library_checkout/static/src/js/checkout.js",
        }
    }
}