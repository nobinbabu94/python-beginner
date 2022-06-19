var express = require('express');
var router = express.Router();

/* GET users listing. */

const isAuth = (req,res,next)=>{
  if(req.session.user){
    next()
  } else{
    res.redirect('/')
  }
}


router.get('/',isAuth, function(req, res,) {
  res.render('landingpage');
});

module.exports = router;
