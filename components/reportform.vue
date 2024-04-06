<template>
    <nav class=" bg-white w-full flex relative justify-between items-center mx-auto px-8 h-20">
    <!-- logo -->
    <div class="inline-flex">
       <img src="/public/logo.png" class="w-44">
    </div>

    <!-- end logo -->
    <!-- login -->
    <div class="flex-initial">
      <div class="flex justify-end items-center relative">
       
        <div class="flex mr-4 items-center">
          <NuxtLink to="login" class="inline-block py-2 px-3  rounded-full" >
            <div class="flex items-center relative cursor-pointer whitespace-nowrap">Log in</div>
          </NuxtLink>
         
        </div>

        <div class="block">
            <div class="inline relative">
                <div class="flex items-center relative cursor-pointer whitespace-nowrap ">About</div>
            </div>
        </div>
      </div>
    </div>
    <!-- end login -->
</nav>


<div class="pt-4 text-2xl"><span class="font-"><center>Professional Website</center><div><span class="text-red-600"><center>Monitoring</center></span></div></span></div>
 
 
      <div class="h-full ml-14 mb-10 md:ml-64 text-black pt-14 pl-24 pr-72 mr-20 ">
        <!-- Endpoint and Bug List -->
        <div class=" flex-col min-w-0 mb-4 lg:mb-0 break-words mx-12 bg-gray-200 mt-8 ">
        
          <div class="dashboard mx-4">
            <main v-if="endpointuri && endpointuri.length">
             
            </main>
            <main v-else>
              <p>No endpoint data available.</p>
            </main>
          </div>
          <!-- Add input field for adding new bugs -->
          <div class="flex flex-col mt-4 py-6 px-4">
            <label for="project" class="text-sm font-medium text-gray-900 ">Select Website:</label>
            <select v-model="selectedProject" id="project" name="project" class="form-select mt-1 block w-full border-gray-300 rounded-md shadow-sm p-0.5">
              <option value="" disabled>-</option>
              <option v-for="project in projects" :key="project" :value="project">{{ project }}</option>
            </select>
          
          <input v-model="newBugTitle" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-full mt-4 p-1.5" placeholder="Title">
          <input v-model="newBugDescription" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-full mt-4 p-1 pb-16" placeholder="Description">
        </div>
          <button @click="addNewBug" class="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 mt-4  w-full">
            REPORT
          </button>
        </div>
      </div>
      <!-- Bug Table -->
      <div class="overflow-x-auto sm:mx-0.5 lg:mx-0.5">
        
      <!-- ./Sidebar -->
     
    

    
      <!-- Header -->
    
      <!-- ./Header -->
      
      </div>
   
    
  </template>
  
  <script>
  import { getFirestore, collection, addDoc, getDocs } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";
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
  const db = getFirestore(app); // Initialize Firestore
  const states = {
    STABLE: "Stable",
    UNSTABLE: "Unstable",
    DOWN: "Down",
  };
  
  export default {
    data() {
      return {
        endpointuri: [],
        newBugTitle: "",
        newBugDescription: "",
        name: "",
        projects: [], // Array to store project URLs
        selectedProject: "", // Variable to store the selected project URL
        bugs: [], // Array to store bugs
      };
    },
    async mounted() {
      await this.fetchData(); // Fetch initial data
      await this.getUser(); // Fetch user data
  
      // Refresh data every 10 seconds
      setInterval(async () => {
        await this.fetchData();
      }, 10000);
    },
    methods: {
      async fetchData() {
        try {
          const endpointsSnapshot = await getDocs(collection(db, "endpointuri"));
          const updatedEndpoints = [];
          const projectURLs = []; // Temporary array to store project URLs
          endpointsSnapshot.forEach((doc) => {
            updatedEndpoints.push({
              id: doc.id,
              ...doc.data(),
            });
            projectURLs.push(doc.data().url); // Push project URL to temporary array
          });
          this.endpointuri = updatedEndpoints;
          this.projects = projectURLs; // Assign project URLs to the data property
  
          // Fetch bugs
          const bugsSnapshot = await getDocs(collection(db, "bugs"));
          const bugs = [];
          bugsSnapshot.forEach((doc) => {
            bugs.push({
              id: doc.id,
              ...doc.data(),
            });
          });
          this.bugs = bugs; // Assign bugs to the data property
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      },
      async addNewBug() {
        try {
          const title = this.newBugTitle.trim();
          const description = this.newBugDescription.trim();
          if (title && description && this.selectedProject) {
            // Add the new bug to Firestore
            await addDoc(collection(db, "bugs"), { title, description, project: this.selectedProject });
  
            // Clear input fields
            this.newBugTitle = "";
            this.newBugDescription = "";
          }
        } catch (error) {
          console.error("Error adding new bug:", error);
        }
      },
      async getUser() {
        try {
          const userData = await getDocs(collection(db, "users"));
          const userDoc = userData.docs[0];
          this.name = userDoc.data().Name;
        } catch (error) {
          console.error("Error fetching user data:", error);
        }
      },
      getStatusWidth(status) {
        switch (status) {
          case states.STABLE:
            return '100%'; // If status is stable, width is 100%
          case states.UNSTABLE:
            return '50%'; // If status is unstable, width is 50%
          case states.DOWN:
            return '30%'; // If status is down, width is 30%
          default:
            return '0%'; // Default width is 0%
        }
      },
      filteredBugs(endpointURL) {
        if (endpointURL) {
          return this.bugs.filter(bug => bug.project === endpointURL);
        } else {
          return this.bugs;
        }
      }
    },
  };
  </script>
  
  <style scoped>
  /* Styles here */
  </style>


<!-- Updated template section -->

  <!-- component -->
 



  