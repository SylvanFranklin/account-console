<script lang="ts">
    export let message: string;
    export let logout: Function;
</script>

<div class="flex flex-col w-1/2 mx-auto mt-20">
    <button
        class="text-white font-mono rounded-sm h-10 w-32 from-green-400 mt-2 bg-gradient-to-r hover:scale-105 duration-75 flex flex-row-reverse items-center justify-center"
        on:click={() => logout()}
    >
        back
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
            ><path
                fill="currentColor"
                d="M17 20V10H7.825l3.6 3.6l-1.4 1.425L4 9l6-6l1.425 1.425L7.825 8H19v12z"
            /></svg
        >
    </button>
    <h1 class="text-white text-2xl font-mono text-center mt-10">
        You logged in
    </h1>
    <p class="text-white font-mono mt-5 text-lg w-1/2">
        {message}
    </p>
</div>
