var RecentCounter = function() {
    this.reqs = []
};

/**
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    if(this.reqs.length == 0) {
        this.reqs.push(t)
    } else {
        while(Math.abs(t - this.reqs[0]) > 3000) {
            this.reqs.shift()
        }
        this.reqs.push(t)
    }

    return this.reqs.length
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */