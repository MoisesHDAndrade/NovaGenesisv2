<template>
    <div>
        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="my-toast">
            <div class="toast-body">
                Hello, world! This is a toast message.
                <div class="mt-2 pt-2 border-top">
                    <button type="button" class="btn btn-primary btn-sm">Take action</button>
                    <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="toast">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:'confirmbox',
    props:[],
    data(){
        return{

        }
    }
}
</script>