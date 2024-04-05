<template>
    <div class="container mx-auto py-8">
      <h1 class="text-3xl font-semibold mb-4">Lista Proiectelor Vercel</h1>
      <div v-if="loading" class="text-gray-600">Se încarcă...</div>
      <div v-else-if="error" class="text-red-600">{{ error }}</div>
      <div v-else>
        <div v-for="project in projects" :key="project.id" class="mb-4">
          <h2 class="text-xl font-semibold">{{ project.name }}</h2>
          <p>Status: {{ project.latestDeploy.status }}</p>
          <div class="mt-2 h-4 bg-gray-200 rounded-full">
            <div :class="[progressColor(project.latestDeploy.status)]" :style="{ width: deploymentProgress(project.latestDeploy.status) + '%' }" class="h-full rounded-full"></div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  
  const vercelToken = 'QUk0AMEPdXtxFBTlu2PGZU39';
  const apiEndPt = 'https://api.vercel.com/v9/projects';
  
  const projects = ref([]);
  const loading = ref(true);
  const error = ref('');
  
  const progressColor = (status) => {
    switch (status) {
      case 'ready':
        return 'bg-green-500';
      case 'building':
        return 'bg-blue-500';
      case 'failed':
        return 'bg-red-500';
      default:
        return 'bg-gray-500';
    }
  };
  
  const deploymentProgress = (status) => {
    switch (status) {
      case 'ready':
        return 100;
      case 'building':
        return 50;
      case 'failed':
        return 0;
      default:
        return 0;
    }
  };
  

axios.get(apiEndPt, {
  headers: {
    Authorization: `Bearer ${vercelToken}`,
  },
})
.then(async (response) => {
  projects.value = await Promise.all(response.data.projects.map(async (project) => {
    try {
      const deployments = await axios.get(`https://api.vercel.com/v12/now/deployments?projectId=${project.id}`, {
        headers: {
          Authorization: `Bearer ${vercelToken}`,
        },
      });
      project.latestDeploy = deployments.data[0] || { status: 'Unknown' };
      return project;
    } catch (deployErr) {
      // Improved error handling
      const status = deployErr.response ? deployErr.response.status : 'Network or other error';
      const message = deployErr.response ? deployErr.response.data : deployErr.message;
      console.error(`Error fetching deployments for project ${project.name}: ${message}`);
      return {
        ...project,
        latestDeploy: { status: 'Unknown', errorStatus: status, message: message }
      };
    }
  }));
  loading.value = false;
})
.catch((err) => {
  // Improved catch block
  const status = err.response ? err.response.status : 'Network or other error';
  const message = err.response ? err.response.data : err.message;
  error.value = `An error occurred: ${message}`;
  console.error(`HTTP Status: ${status}, Error: ${message}`);
  loading.value = false;
});

  </script>
  
  <style scoped>
  /* Add your CSS styles here */
  .bg-gray-500 {
    background-color: #d1d5db;
  }
  
  .bg-green-500 {
    background-color: #22c55e;
  }
  
  .bg-blue-500 {
    background-color: #60a5fa;
  }
  
  .bg-red-500 {
    background-color: #ef4444;
  }
  </style>
  