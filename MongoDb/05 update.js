db.inventory.updateOne({
    item:"paper"
},
{
    $set:{"size.uom":"cm",status:"p"},
    $currentDate:{lastModified: true}
})
//used to update the database in your collectons
