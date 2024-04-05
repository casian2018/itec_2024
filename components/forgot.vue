<template>

    <!-- component -->
<link rel="stylesheet" href="https://kit-pro.fontawesome.com/releases/v5.15.1/css/pro.min.css" />

<div class="min-h-screen flex flex-col items-center justify-center bg-gray-300">
  <div class="flex flex-col bg-white shadow-md px-4 sm:px-6 md:px-8 lg:px-10 py-8 rounded-md w-full max-w-md">
   
   
    <div class="mt-0">
      <form @submit.prevent="login">
        <div class="flex flex-col mb-4">
          <label for="email" class="mb-1 text-xs sm:text-sm tracking-wide text-gray-600">Enter e-mail address:</label>
          <div class="relative">
            <div class="inline-flex items-center justify-center absolute left-0 top-0 h-full w-10 text-gray-400">
              <svg class="h-6 w-6" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
              </svg>
            </div>

            <input id="email" type="email" name="email" class="text-sm sm:text-base placeholder-gray-500 pl-10 pr-4 rounded-lg border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400" placeholder="E-Mail Address" v-model="email"/>
          </div>
        </div>
        

        

        <div class="flex w-full">
          <button type="submit" class="flex  focus:outline-none text-white text-sm sm:text-base bg-gray-500 hover:bg-gray-600 rounded py-2 w-15 transition duration-150 ease-in">
            <span class="mr-2 ml-2 text-sm " @click="sendPasswordResetEmail">Reset your password</span>
            <span>
              
            </span>
          </button>
        </div>
      </form>
    </div>
    
  </div>
</div>

</template>




<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp} from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyDTXWIiULSBECNDYj8D6U3pio0TTjyNuCc",
    authDomain: "itec2024.firebaseapp.com",
    projectId: "itec2024",
    storageBucket: "itec2024.appspot.com",
    messagingSenderId: "654897749335",
    appId: "1:654897749335:web:86ad18e39b11b730a1b212",
    measurementId: "G-V38WHRYJ7R"
  };

  const app = initializeApp(firebaseConfig);


  // Initialize Firebase
  

  // Import Firebase Authentication
  import { getAuth, sendPasswordResetEmail } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-auth.js";

  const auth = getAuth();

 

  export default {
    data() {
      return {
        email: ' '
      }
    },
    methods: {
    async sendPasswordResetEmail() {
        try {
            await sendPasswordResetEmail(auth, this.email)
            // Password reset email sent!
            //..
        } catch (error) {
            const errorCode = error.code;
            const errorMessage = error.message;
            //..
        }
    }
}
  }

  
  


  
</script>