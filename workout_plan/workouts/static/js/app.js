console.log("Custom Workout Schedule")


let showLoading = () => {
  document.getElementById('generate-schedule').setAttribute('class', 'btn btn-primary btn-lg btn-block disabled')
  document.getElementById('generate-schedule').innerHTML = 'Generating Custom Schedule...'
}
