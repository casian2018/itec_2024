<template>
<nav class="fixed bg-white w-full flex justify-between items-center mx-auto px-8 h-20 ">
    <div class="inline-flex">
       <a href="/"><img src="/public/logo.png" class="w-44"></a>
    </div>
    <div class="flex-initial">
      <div class="flex justify-end items-center relative">
       
        <div class="flex mr-4 items-center">
          <NuxtLink to="login" class="inline-block py-2 px-3  rounded-full" >
            <div class="flex items-center relative cursor-pointer whitespace-nowrap">Log in</div>
          </NuxtLink>
         
        </div>

        <div class="block">
            <div class="inline relative">
                <NuxtLink to="contact">Contact</NuxtLink>
            </div>
        </div>
      </div>
    </div>
</nav>
</template>