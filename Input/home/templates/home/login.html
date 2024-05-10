<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login Form</title>
    <script
      type="text/javascript"
      src="https://unpkg.com/webcam-easy/dist/webcam-easy.min.js"
    ></script>
    <link
      href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css"
      rel="stylesheet"
    />
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@700&family=Poppins:wght@400;500;600&display=swap");
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
      }
      body {
        margin: 0;
        padding: 0;
        background: rgb(2, 0, 36);
        background: linear-gradient(
          90deg,
          rgb(133, 130, 177) 0%,
          rgba(182, 168, 108, 0.981) 35%,
          rgb(126, 171, 180) 700%
        );
        height: 100vh;
        overflow: hidden;
      }
      .center {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 400px;
        max-width: 90%;
        background: white;
        max-height: 90%;
        overflow: auto;
        border-radius: 10px;
        box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.05);
        text-align: center; /* Center align contents */
      }

      .center::-webkit-scrollbar {
        display: none;
      }
      .center h1 {
        text-align: center;
        padding: 20px 0;
        border-bottom: 1px solid silver;
      }
      .center form {
        padding: 0 40px;
        box-sizing: border-box;
      }
      form .txt_field {
        position: relative;
        border-bottom: 2px solid #adadad;
        margin: 30px 0;
      }
      .txt_field input {
        width: 100%;
        padding: 0 5px;
        height: 40px;
        font-size: 16px;
        border: none;
        background: none;
        outline: none;
      }
      .txt_field label {
        position: absolute;
        top: 50%;
        left: 5px;
        color: #adadad;
        transform: translateY(-50%);
        font-size: 16px;
        pointer-events: none;
        transition: 0.5s;
      }
      .txt_field span::before {
        content: "";
        position: absolute;
        top: 40px;
        left: 0;
        width: 0%;
        height: 2px;
        background: #2691d9;
        transition: 0.5s;
      }
      .txt_field input:focus ~ label,
      .txt_field input:valid ~ label {
        top: -5px;
        color: #2691d9;
      }
      .txt_field input:focus ~ span::before,
      .txt_field input:valid ~ span::before {
        width: 100%;
      }
      .pass {
        margin: 20px 0; /* Adjust margin as needed */
        text-align: center;
        color: #a6a6a6;
        cursor: pointer; 
        display: inline-block; /* Ensure inline display */
      }
      .pass:hover {
        text-decoration: underline;
      }
      input[type="submit"] {
        width: 100%;
        height: 50px;
        border: 1px solid;
        background: #25353f;
        border-radius: 25px;
        font-size: 18px;
        color: #e9f4fb;
        font-weight: 700;
        cursor: pointer;
        outline: none;
        margin-top: 20px; /* Add margin top to space from capture link */
      }
      input[type="submit"]:hover {
        border-color: #364550;
        transition: 0.5s;
      }
      .signup_link {
        margin: 30px 0;
        text-align: center;
        font-size: 16px;
        color: #666666;
      }
      .signup_link a {
        color: #1c2023;
        text-decoration: none;
      }
      .signup_link a:hover {
        text-decoration: underline;
      }
      #image {
        display: none;
      }
    </style>
  </head>
  <body>
    <div class="center">
      <form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <h1>Login</h1>
        <div class="txt_field">
          <input type="text" name="username" required />
          <span></span>
          <label>Username</label>
        </div>
        <div class="txt_field">
          <input type="password" name="password" required />
          <span></span>
          <label>Password</label>
        </div>
        <video id="webCam" autoplay playsinlne width="350" height="250"></video>
        <canvas id="canvas" width="30" height="15"></canvas>
        <a class="pass" onClick="takePicture()">Capture</a>
        <!-- capture photo karna hai  -->
        <input type="text" id="image" name="image" accept="image/*" />
        <br />

        <input type="submit" value="Login" />
        <div class="signup_link">Not a member? <a href="#">Signup</a></div>
      </form>
    </div>
    <div class="error-message">
      {% if error %}
      <p>
        Incorrect username or password. Please recheck your credentials and try
        again.
      </p>
      {% endif %}
    </div>
    <script>
      const imageDataInput = document.getElementById("image");
      const webcamElement = document.getElementById("webCam");
      const canvasElement = document.getElementById("canvas");
      const webcam = new Webcam(webcamElement, "user", canvasElement);
      webcam.start();
      function takePicture() {
        let picture = webcam.snap();
        document.querySelector("a").href = picture;
        console.log("Captured picture:", picture);
        imageDataInput.setAttribute("value", picture);
      }
    </script>
  </body>
</html>