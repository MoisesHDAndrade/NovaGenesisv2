<template>
    <div></div>
</template>

<script>
export default {
    methods:{
        toaster(obj){
            const toastMixin = Swal.mixin({
                toast: true,
                position: 'top-end',
                
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
            });
    
            toastMixin.fire({
                // animation: true,
                icon: obj.type,
                title: obj.message
            });
    
        },
        
    },
    

}
</script>