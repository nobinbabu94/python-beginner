var express = require('express');
  var router = express.Router();


let userName = "nobins73@gmail.com"
let pass = "1234"

router.get('/', function (req, res, next) {
  if(req.session.user){
    res.redirect('/users')

  } else{
     res.render('index', { title: 'Express' });
  }
});

router.post('/login', (req, res) => {
  const {Email,Password }  = req.body;
  
  if(userName === Email && pass === Password){

    req.session.user = {
      userName
    }
    res.redirect('/users')

  } else{
    res.redirect('/')
  }
})

router.get('/logout',(req,res)=>{
  req.session.destroy();
  res.redirect('/');
})

module.exports = router;