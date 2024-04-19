// Copyright (c) 2024, Emmanuel Mwendwa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Article", {
  refresh: function (frm) {
    frm.add_custom_button("Create Transaction", () => {
      frappe.new_doc("Library Transaction", {
        article: frm.doc.name,
      });
    });
  },
});
