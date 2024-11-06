<script lang="ts">
    import AccountPage from "$lib/account_page.svelte";
    import { fly, scale } from "svelte/transition";
    let signup: boolean = true;
    let loggedIn: boolean = false;
    let userData: string = "";
    let error = "";

    function handle_form_submit(e: SubmitEvent) {
        let url = "http://127.0.0.1:5000/" + (signup ? "register" : "login");
        const formData = new FormData(e.target as HTMLFormElement);
        let request = new XMLHttpRequest();
        request.open("POST", url, true);
        request.send(formData);
        request.onload = function () {
            if (request.responseText.startsWith("SUCCESS")) {
                userData = request.responseText.split("SUCCESS: ")[1];
                loggedIn = true;
            } else if (request.responseText.startsWith("NEW")) {
                userData = request.responseText.split("WELCOME NEW GUY: ")[1];
                loggedIn = true;
            } else {
                error = request.responseText.split("ERROR: ")[1];
            }
        };

        request.onerror = function () {
            error = "backend not running";
        };
    }
</script>

<main class="bg-black h-screen w-screen flex flex-col items-center">
    {#if loggedIn}
        <AccountPage message={userData} logout={() => (loggedIn = false)} />
    {:else}
        <h1
            class="bg-gradient-to-r from-blue-300 via-red-300 to-white inline-block text-transparent bg-clip-text font-mono text-5xl mt-10 font-bold select-none"
        >
            Account Console
        </h1>
        <p class="text-white font-mono mt-5 text-lg w-1/2">
            Jake, Luke, and Sylvan, user database + login page demo.
        </p>

        <nav class="flex flex-row gap-3 mt-6">
            {#if signup}
                <button
                    class="text-white font-mono rounded-sm h-10 w-32 bg-gradient-to-l from-red-400 mt-2 hover:scale-105 duration-75"
                    on:click={() => (signup = false)}
                >
                    login
                </button>
            {:else}
                <button
                    class="text-white font-mono rounded-sm h-10 w-32 from-blue-400 mt-2 bg-gradient-to-r hover:scale-105 duration-75"
                    on:click={() => (signup = true)}
                >
                    register
                </button>
            {/if}
        </nav>

        <div
            class="flex flex-col items-center mx-auto rounded-md sm:w-3/4 lg:w-2/5 p-8"
        >
            {#if error}
                <p class="text-red-400 font-mono text-center">
                    {error}
                </p>
            {/if}
            <form
                on:submit|preventDefault={handle_form_submit}
                class="flex flex-col gap-4 justify-center items-center p-4 mt-4 w-full h-full text-black bg-none rounded-xl shadow-lg"
            >
                <input
                    type="text"
                    name="username"
                    in:scale={{ duration: 200 }}
                    placeholder="username..."
                    class="w-full h-12 font-mono text-xl text-white p-3 rounded-lg bg-gray-400/20 border-white outline-none"
                />
                <input
                    in:scale={{ duration: 200, delay: 5 }}
                    name="password"
                    type="password"
                    placeholder="password..."
                    class="w-full h-12 font-mono text-xl text-white p-3 rounded-lg bg-gray-400/20 border-white outline-none"
                />

                {#if signup}
                    <input
                        type="text"
                        in:scale={{ duration: 200, delay: 10 }}
                        name="firstname"
                        placeholder="firstname..."
                        class="w-full h-12 font-mono text-xl text-white p-3 rounded-lg bg-gray-400/20 border-white outline-none dark:text-white"
                    />
                    <input
                        type="text"
                        in:scale={{ duration: 200, delay: 15 }}
                        name="lastname"
                        placeholder="lastname..."
                        class="w-full h-12 font-mono text-xl text-white p-3 rounded-lg bg-gray-400/20 border-white outline-none dark:text-white"
                    />
                {/if}
                <button
                    in:fly={{ duration: 300, y: 100 }}
                    type="submit"
                    class="font-mono flex flex-row justify-center gap-2 items-center bg-gray-400/20 rounded-md hover:scale-105 duration-100 h-12 w-44 text-white"
                >
                    {#if signup}
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 24 24"
                            ><path
                                fill="currentColor"
                                d="M18 14v-3h-3V9h3V6h2v3h3v2h-3v3zm-9-2q-1.65 0-2.825-1.175T5 8t1.175-2.825T9 4t2.825 1.175T13 8t-1.175 2.825T9 12m-8 8v-2.8q0-.85.438-1.562T2.6 14.55q1.55-.775 3.15-1.162T9 13t3.25.388t3.15 1.162q.725.375 1.163 1.088T17 17.2V20z"
                            /></svg
                        > sign up
                    {:else}
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 24 24"
                            ><path
                                fill="currentColor"
                                d="M9 2h9c1.1 0 2 .9 2 2v16c0 1.1-.9 2-2 2H9c-1.1 0-2-.9-2-2v-2h2v2h9V4H9v2H7V4c0-1.1.9-2 2-2"
                            /><path
                                fill="currentColor"
                                d="M10.09 15.59L11.5 17l5-5l-5-5l-1.41 1.41L12.67 11H3v2h9.67z"
                            /></svg
                        >
                        login
                    {/if}
                </button>
            </form>
        </div>
    {/if}
</main>
