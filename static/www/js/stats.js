function setLiveStatus(data){
    const live_status = document.getElementById('liveStatus');
    live_status.innerText = 'Live';
    const live_status_refreshed = document.getElementById('live-status-refreshed');
    live_status_refreshed.innerText = data['date'];
}
function calcViewsChange(value_today, value_yesterday) {
    return ((value_today / value_yesterday) - 1)*100;
}
function setViewsChange(data) {
    const all_views_change = document.getElementById('all-views-change');
    let change_value = calcViewsChange(data['all_entries_today'], data['all_entries_yesterday']);
    if(change_value>=0) {
        all_views_change.classList.add('text-success');
        all_views_change.classList.remove('text-danger');
        all_views_change.innerText = '+' + change_value.toFixed(2) + '%';
    } else {
        all_views_change.classList.add('text-danger');
        all_views_change.classList.remove('text-success');
        all_views_change.innerText = change_value.toFixed(2) + '%';
    }
}
function setCounters(data) {
    //Get counter elements
    const all_views_counter = document.getElementById('allViewsCount');
    const index_views_counter = document.getElementById('IndexViewsCount');
    const cv_views_counter = document.getElementById('CVViewsCount');
    //Set counters
    all_views_counter.innerText = data['all_entries_today'];
    index_views_counter.innerText = data['index_entries_today'];
    cv_views_counter.innerText = data['cv_entries_today'];
    setViewsChange(data);
    //Set refreshed status
    setLiveStatus(data);
}
function getStats() {
    fetch('/api/stats')
        .then(response => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error(`API error (${response.status})`);
            }
        })
        .then(data => {
            setCounters(data);
        }).catch(error => {
            console.log(error);
    })
}
getStats();
setInterval(getStats, 5000);