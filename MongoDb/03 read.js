db.inventory.find()
//fetch all documents
db.inventory.find({qty:90})
//u can find it from pulling it from database


//AND
db.inventory.find({status:"A",qty:{$lt:30}})

//OR
db.inventory.find({$or:{status:}A},{qty:{$lt:30}})

//only pull if it true and conditon will be true