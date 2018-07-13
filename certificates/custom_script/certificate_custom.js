var count=1
frappe.ui.form.on("Certificate", "add_more_attachment", function(frm, cdt, cdn) {
count=count+1
if(count==2)
{
	frm.fields_dict.attachment_2.df.hidden=0
	frm.refresh_field("attachment_2");
	console.log(frm);
}
if(count==3)
{
	frm.fields_dict.attachment_3.df.hidden=0
	frm.refresh_field("attachment_3");
	console.log(frm);
}
if(count==4)
{
	frm.fields_dict.attachment_4.df.hidden=0
	frm.refresh_field("attachment_4");
	console.log(frm);
}
if(count==5)
{
	frm.fields_dict.attachment_5.df.hidden=0
	frm.refresh_field("attachment_5");
	console.log(frm);
}


})
