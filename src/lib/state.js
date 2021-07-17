import { writable } from 'svelte/store';

export const actionIndex = writable(0);
export const clickStart = writable(false);
export const defaultPopup = writable(false);
export const setupFinish = writable(false);
export const debug = writable(false);

export const history = writable({
    age : {

    },
    gender : {

    },
    race : {

    },
    installCal : {
        
    }
});