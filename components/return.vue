<template>

<link rel="stylesheet" href="https://kit-pro.fontawesome.com/releases/v5.15.1/css/pro.min.css" />

<div class="min-h-screen flex flex-col items-center justify-center bg-gray-300">
  <div class="flex flex-col bg-white shadow-md px-4 sm:px-6 md:px-8 lg:px-10 py-8 rounded-md w-full max-w-md">
   
   
    <div class="mt-0">
      <form @submit.prevent="login">
        <div class="flex flex-col mb-4">
          
          <div class="relative">
            <div class="inline-flex items-center justify-center absolute left-0 top-0 h-full w-10 text-gray-400">
             
            </div>

            <span>E-mail sent</span>
          </div>
        </div> 

        <div class="flex w-full">
          <button type="submit" class="flex  focus:outline-none text-white text-sm sm:text-base bg-gray-500 hover:bg-gray-600 rounded py-2 w-15 transition duration-150 ease-in">
            <NuxtLink to="login"><span class="mr-2 ml-2 text-sm ">Return to login page</span></NuxtLink>
            <span>
              
            </span>
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>


<script>
import { getFirestore, collection, getDocs } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";

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
const db = getFirestore(app); 

export default {
  data() {
    return {
      bugs: []
    };
  },
  async fetch() {
    await this.loadBugs();
  },
  methods: {
    async loadBugs() {
      try {
        const bugsSnapshot = await getDocs(collection(db, "bugs"));
        const bugs = bugsSnapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));
        this.bugs = bugs;
      } catch (error) {
        console.error("Error fetching bugs:", error);
      }
    }
  }
};
</script>






