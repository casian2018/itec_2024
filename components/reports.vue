<template>
  <!-- Component -->
  <div x-data="setup()" :class="{ 'dark': isDark }">
    <!-- Header -->
    <div class="fixed w-full flex items-center justify-between h-14 text-white z-[99]">
      <div class="flex items-center justify-start md:justify-center pl-3 w-14 md:w-64 h-14 dark:bg-blue-900  border-none]">
        <span class="hidden md:block">{{ name }}</span>
      </div>
      <div class="flex justify-between items-center h-14 bg-blue-800 dark:bg-gray-800 header-right">
        <ul class="flex items-center"></ul>
      </div>
    </div>
    <!-- ./Header -->
    <!-- Sidebar -->
    <!-- Sidebar -->
    <div class="fixed flex flex-col top-14 left-0 w-14 hover:w-64 md:w-64  bg-blue-600 h-full text-white transition-all duration-300 border-none sidebar">
      <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
        <ul class="flex flex-col py-4 space-y-1">
          <li class="px-5 hidden md:block">
            <div class="flex flex-row items-center h-8">
              <div class="text-sm font-light tracking-wide text-white uppercase"></div>
            </div>
          </li>
          <li>
            <NuxtLink to="dash" class="relative flex flex-row items-center h-11 focus:outline-none  border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
              <span class="inline-flex justify-center items-center ml-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
              </span>
              <span class="ml-2 text-sm tracking-wide truncate text-gray-400">Dashboard</span>
            </NuxtLink>
          </li>
          <li>
            <NuxtLink to="reports" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-700 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
              <span class="inline-flex justify-center items-center ml-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
              </span>
              <span class="ml-2 text-sm tracking-wide truncate">Reports</span>
              <span class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-blue-500 bg-indigo-50 rounded-full">New</span>
            </NuxtLink>
          </li>
        </ul>
      </div>
    </div>
    <!-- ./Sidebar -->
    <div class="h-full ml-14 mb-10 md:ml-64 text-black">
      <!-- Endpoint and Bug List -->
      <div class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words mx-12 bg-gray-200 mt-8 rounded-xl">
        <div class="rounded-t mb-0 px-0 border-0 ">
          <div class="flex flex-wrap items-center px-4 py-2 "></div>
        </div>
        <div class="dashboard mx-4">
          <main v-if="endpointuri && endpointuri.length">
            <div v-for="endpoint in endpointuri" :key="endpoint.id" class="endpoint-item grid grid-cols-3 mt-6">
              <div class="col-span-3">
                <p class="endpoint-url p-1">{{ endpoint.url }}</p>
                <p class="endpoint-status">
                  Status: {{ endpoint.status }}
                  <span class="ml-2 text-xs font-medium rounded-full px-1"></span>
                </p>
                <div class="w-full rounded">
                  <div :class="`bg-blue-500 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded`"
                    :style="{ width: getStatusWidth(endpoint.status) }">
                  </div>
                </div>
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
                    <tr v-for="bug in endpoint.bugs" :key="bug.id">
                      <td class="border px-4 py-2">{{ bug.title }}</td>
                      <td class="border px-4 py-2">{{ bug.description }}</td>
                      <td class="border px-4 py-2">{{ endpoint.url }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </main>
          <main v-else>
            <p>No endpoint data available.</p>
          </main>
        </div>
        <!-- Add input field for adding new links -->
        <button @click="addNewEndpoint" class="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 ml-64 rounded  mb-4 w-36">
          Add New Link
        </button>
        <input v-model="newEndpointUrl" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-48 h-8 ml-12">
      </div>
    </div>
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
      newEndpointUrl: "",
      name: "",
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
          await addDoc(collection(db, "endpointuri"), { url, status: "", bugs: [], project: url });
          await this.fetchData(); // Fetch updated data
          this.newEndpointUrl = ""; // Clear input field
        }
      } catch (error) {
        console.error("Error adding new endpoint:", error);
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
  },
};
</script>

<style scoped>
/* Styles here */
</style>
