<!-- Updated template section -->
<template>
  <!-- component -->
  <div x-data="setup()" :class="{ 'dark': isDark }">
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
                <span class="ml-2 text-sm tracking-wide truncate text-gray-400">Dashboard</span>
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="report" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-700 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                <span class="inline-flex justify-center items-center ml-4">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                </span>
                <span class="ml-2 text-sm tracking-wide truncate">Reports</span>
                <span class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-blue-500 bg-indigo-50 rounded-full">New</span>
              </NuxtLink>
            </li>
          
            <!-- Other sidebar items -->
          </ul>
        </div>
      </div>
      <!-- ./Sidebar -->
      <div class="h-full ml-14 mb-10 md:ml-64 text-black">
        <!-- Social Traffic -->
        <div class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words mx-12 bg-gray-200 mt-8 rounded-xl">
          <div class="rounded-t mb-0 px-0 border-0 ">
            <div class="flex flex-wrap items-center px-4 py-2 "></div>
          </div>
          <div class="dashboard mx-4">
            <main v-if="endpointuri && endpointuri.length">
              <div v-for="endpoint in endpointuri" :key="endpoint.id" class="endpoint-item grid grid-cols-4 mt-6">
                <p class="endpoint-url ">{{ endpoint.url }}</p>
                <p class="endpoint-status ">
                  Status: {{ endpoint.status }}
                  <span class="ml-2 text-xs font-medium rounded-full px-1"></span>
                </p>
               
                  <div class="bg-blue-500 text-xs font-medium  ml-16  p-1  mb-2 mt-4 leading-none rounded"
                    :style="{ width: getStatusWidth(endpoint.status) }">
                    
                  </div>
                  <div class="rounded ">
                  <button @click="removeEndpoint(endpoint.id)" class="bg-red-500 hover:bg-red-600 text-white font-medium rounded ml-52 mt-2 w-4 h-4 text-xs">
                  X
                </button>
                  
                </div>
                
                
              </div>
            </main>
            <main v-else>
              <p>No endpoint data available.</p>
            </main>
          </div>
          <div class="grid grid-cols-4 ">
            <div>
          <button @click="addNewEndpoint" class=" bg-blue-500 hover:bg-blue-600 text-white font-medium py-2  ml-12 rounded  mb-4 w-48 mt-8 ">
              Add New Link
            </button>
          <!-- Add input field for adding new links -->
          <input v-model="newEndpointUrl" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-48 h-8 ml-12 mb-4" placeholder=" www.web.com">
          </div>
          <div>
          <button @click="addNewEndpoint" class=" bg-blue-500 hover:bg-blue-600 text-white font-medium py-2  ml-12 rounded  mb-4 w-48 mt-8 ">
              Refresh every "x" seconds
            </button>
          <!-- Add input field for adding new links -->
          <input v-model="newEndpointUrl" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-48 h-8 ml-12 mb-4" placeholder=" x">
          </div>
         

         
        </div>
            
            
     
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getFirestore, collection, addDoc, getDocs, deleteDoc, doc } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";
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
      newEndpointUrl: "",
      name: "",
    };
  },
  async mounted() {
    await this.fetchData(); // Fetch initial data
    setInterval(async () => {
      await this.fetchData(); // Fetch data every 10 seconds
    }, 10000);
  },
  methods: {
    async fetchData() {
      try {
        const endpointsSnapshot = await getDocs(collection(db, "endpointuri"));
        const updatedEndpoints = [];
        endpointsSnapshot.forEach((doc) => {
          updatedEndpoints.push({
            id: doc.id,
            ...doc.data(),
          });
        });
        this.endpointuri = updatedEndpoints;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    async addNewEndpoint() {
      try {
        const url = this.newEndpointUrl.trim();
        if (url) {
          await addDoc(collection(db, "endpointuri"), { url, status: "" });
          await this.fetchData(); // Fetch updated data
          this.newEndpointUrl = ""; // Clear input field
        }
      } catch (error) {
        console.error("Error adding new endpoint:", error);
      }
    },
    async removeEndpoint(endpointId) {
      try {
        await deleteDoc(doc(db, "endpointuri", endpointId));
        this.endpointuri = this.endpointuri.filter(endpoint => endpoint.id !== endpointId);
      } catch (error) {
        console.error("Error removing endpoint:", error);
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
  margin: 5px ;
}
</style>