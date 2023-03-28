<template>
    <div></div>
</template>

<script>
export default {
    props:[
        'message',
        'type'
    ],
    methods:{
        async confirmation(obj){
            console.log(obj)
            let confirmDelete = false
            const confirm = await Swal.mixin({
                customClass: {
                    confirmButton: 'btn bg-warning-light m-2 shadow-none text-dark',
                    cancelButton: 'btn btn-dark shadow-none',
                    closeButton:'btn bg-yellow  shadow-none text-dark'
                    },
                    buttonsStyling: false
                })
                confirm.fire({
                    title: obj.typeMsg,
                    // text: "You won't be able to revert this!",
                    text: obj.askingMsg,
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonText: 'Yes, delete it!',
                    cancelButtonText: 'No, cancel!',
                    reverseButtons: true,
                    
                    }).then((result) => {
                        if (result.isConfirmed) {
                            
                            // swal.fire(
                            // 'Deleted!',
                            // confirmedMsg,
                            // 'success'
                            // )
                            this.$emit('delete', obj)
                        } 
                        else if (
                            /* Read more about handling dismissals below */
                            result.dismiss === Swal.DismissReason.cancel
                            
                        ) {
                        
                        confirm.fire(
                            'Cancelled',
                            obj.cancelledMsg,
                            'error',
                            )
                        }
                 })
        },
        triggerToast(){
            this.toaster()
        }
    },
    mounted(){
        // this.$root.$on('messageConfirmation', data => {
        //     this.confirmation( data.obj, data.typeMsg, data.askingMsg, data.confirmedMsg, data.cancelledMsg);
        // });
    },
    created(){
    }

}
</script>