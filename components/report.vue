<template>
    <!- <div x-data="setup()" :class="{ 'dark': isDark }">
    <div
      class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-white-500 text-black dark:text-white">
      <!-- Header -->
      <div class="fixed w-full flex items-center justify-between h-14 text-white z-10">
        <div
          class="flex items-center justify-start md:justify-center pl-3 w-14 md:w-64 h-14 dark:bg-blue-900  border-none">
          <span class="hidden md:block">ADMIN PANEL</span>
        </div>
        <div class="flex justify-between items-center h-14 bg-blue-800 dark:bg-gray-800 header-right">
          <ul class="flex items-center"></ul>
        </div>
      </div>
      <!-- ./Header -->
      <!-- Sidebar -->
      <!-- Sidebar -->
      <div class="fixed flex flex-col top-14 left-0 w-14 hover:w-64 md:w-64  bg-blue-600 h-full text-white transition-all duration-300 border-none z-10 sidebar">
        <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
          <ul class="flex flex-col py-4 space-y-1">
            <li class="px-5 hidden md:block">
              <div class="flex flex-row items-center ">
                <div class="text-sm font-light tracking-wide text-white uppercase"></div>
              </div>
            </li>
            <li >
              <NuxtLink to="dash" class="relative flex flex-row items-center h-11 focus:outline-none  border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                <span class="inline-flex justify-center items-center ml-4">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                </span>
                <span class="ml-2 text-sm tracking-wide truncate ">Dashboard</span>
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="report" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-700 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                <span class="inline-flex justify-center items-center ml-4">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                </span>
                <span class="ml-2 text-sm tracking-wide truncate text-gray-400">Reports</span>
                <span class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-blue-500 bg-indigo-50 rounded-full">New</span>
              </NuxtLink>
            </li>
          
            <!-- Other sidebar items -->
          </ul>
        </div>
      </div>

      <div class="h-full ml-14 mb-10 md:ml-64 text-black">
        <!-- Endpoint and Bug List -->
        <div class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words mx-12 bg-gray-200 mt-8 rounded-xl">
        
          <div class="dashboard mx-4 pb-6">
            <main v-if="endpointuri && endpointuri.length">
              <div v-for="endpoint in endpointuri" :key="endpoint.id" class="endpoint-item grid grid-cols-3 mt-6">
                <div class="col-span-3">
                  <p class="endpoint-url p-1">{{ endpoint.url }} <span class="pl-4">{{ endpoint.status }}</span></p>
                  
                
                  
                 
                </div>
                <div class="col-span-3 mt-2">
                  <table class="w-full table-auto">
                    <thead>
                      <tr>
                        <th class="px-4 py-2">Bug Title</th>
                        <th class="px-4 py-2">Bug Description</th>
                        <th class="px-4 py-2">Project</th>
                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(bug, index) in filteredBugs(endpoint.url)" :key="index" class="bg-gray-100 border-b">
                        <td class="border px-4 py-2">{{ bug.title }}</td>
                        <td class="border px-4 py-2">{{ bug.description }}</td>
                        <td class="border px-4 py-2">{{ bug.project }}</td>
                        
                      </tr>
                      
                    </tbody>
                    
                  </table>
                  <br>
                  <p class="border-2 border-blue-500" pt-4></p>
                  
                </div>
                
              </div>
              
            </main>
            <main v-else>
              <p>No endpoint data available.</p>
            </main>
          </div>
          <!-- Add input field for adding new bugs -->
         
         
        </div>
      </div>
      <!-- Bug Table -->
    

    
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
 



  