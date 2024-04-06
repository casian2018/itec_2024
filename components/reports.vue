<template>
    <!-- component -->
    <div x-data="setup()" :class="{ 'dark': isDark }">
      <div class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-white-500 text-black dark:text-white">
        <!-- Header -->
        <div class="fixed w-full flex items-center justify-between h-14 text-white z-10">
          <div class="flex items-center justify-start md:justify-center pl-3 w-14 md:w-64 h-14 dark:bg-blue-900  border-none">
            <span class="hidden md:block">{{ name }}</span>
          </div>
          <div class="flex justify-between items-center h-14 bg-blue-800 dark:bg-gray-800 header-right">
            <ul class="flex items-center"></ul>
          </div>
        </div>
        <!-- ./Header -->
        <!-- Sidebar -->
        <div class="fixed flex flex-col top-14 left-0 w-14 hover:w-64 md:w-64  bg-blue-600 h-full text-white transition-all duration-300 border-none z-10 sidebar">
          <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
            <ul class="flex flex-col py-4 space-y-1">
              <li class="px-5 hidden md:block">
                <div class="flex flex-row items-center h-8">
                  <div class="text-sm font-light tracking-wide text-white uppercase">Main</div>
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
                <NuxtLink to="reports" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-700 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
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
        <!-- ./Sidebar -->
       
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
  
  const states = {
    STABLE: "Stable",
    UNSTABLE: "Unstable",
    DOWN: "Down",
  };
  
  export default {
    data() {
      return {
        endpointuri: [],
        name: "",
      };
    },
    async mounted() {
      const app = initializeApp(firebaseConfig);
      const db = getFirestore(app);
  
      const fetchEndpoints = async () => {
        try {
          const endpointsSnapshot = await getDocs(collection(db, "endpointuri"));
          const updatedEndpoints = [];
  
          endpointsSnapshot.forEach((doc) => {
            const endpointData = doc.data();
            const recentCalls = endpointData.callHistory ? endpointData.callHistory.slice(-10) : [];
            const status = calculateStatus(recentCalls);
  
            updatedEndpoints.push({
              id: doc.id,
              ...endpointData,
              status,
              statusWidth: calculateStatusWidth(status),
            });
          });
  
          this.endpointuri = updatedEndpoints;
        } catch (error) {
          console.error("Error fetching endpoints:", error);
        }
      };
  
      const calculateStatus = (recentCalls) => {
        if (recentCalls.every((call) => call.statusCode === 200 || call.statusCode === 302)) {
          return states.STABLE;
        } else if (recentCalls.some((call) => call.statusCode !== 200 && call.statusCode !== 302)) {
          return states.UNSTABLE;
        } else {
          return states.DOWN;
        }
      };
  
      const calculateStatusWidth = (status) => {
        switch (status) {
          case states.STABLE:
            return 100;
          case states.UNSTABLE:
            return 50;
          case states.DOWN:
            return 0;
        }
      };
  
      const getUser = async () => {
        try {
          const userData = await getDocs(collection(db, "users"));
  
          // Get the first user document
          const userDoc = userData.docs[0];
  
          // Set the name input field value to the user's name
          this.name = userDoc.data().Name;
        } catch (error) {
          console.error("Error fetching endpoints:", error);
        }
      };
  
      // Initial fetch
      getUser();
  
      // Refresh endpoint data every second
      setInterval(fetchEndpoints, 1000);
    },
  };
  </script>
  
  <style scoped>
  .dashboard {
    padding: 20px;
    color: black;
  } 
  .navbar {
    background-color: #2196F3;
    color: #fff;
    padding: 10px 20px;
  }
  
  .navbar-title {
    margin: 0;
    
  }
  
  .endpoint-list {
    margin-top: 20px;
    
  }
  
  .endpoint-item {
    background-color: #f4f4f4;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .endpoint-url {
    margin: 0;
  }
  
  .endpoint-status {
    margin: 5px 0;
  }
  </style>
  