function validate() {
    var email = document.getElementById("email").value; 
    var password = document.getElementById("password").value;
    if(email == "admin" && password == "user"){
    alert("login successfully");
    }
    else
    {
    alert("login failed");
    }
}

function checkPassword(){
    let password = document.getElementById("password").value;
    let confirmpassword = document.getElementById("confirmpassword").value;
    console.log(password, confirmpassword);
    let message = document.getElementById("message");
  
    if (password.length != 0){
      if (password == confirmpassword){
        message.textContent = "Password Match";
        message.style.backgroundColor = "#3ae374";
      }
        else{
          message.textContent = "Password Does Not Match";
          message.style.backgroundColor = "#ff4d4d";
        }
    }
    else{
      alert("Password can't be empty");
      message.textContent = "";
    }
  }