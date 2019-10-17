/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    if (path.length === 0) {
        return ""
    }

    stack = []
    let i = 0
    let dir = ""
    while(i < path.length) {

        while(i < path.length && path[i] === "/") {
            i++
            dir = ""
        }


        if(path[i] === "." && path[i+1] === "." && path[i+2] === ".") {
            while(path[i] === ".") {
                dir += path[i]
                i++
            }

        } else if (path[i] === "." && path[i+1] === "." && (i+2 >= path.length || path[i+2] === "/")) {
            stack.pop()
            i += 2
            continue
        } else if (path[i] === "." && (path[i+1] === "/" || i+1 >= path.length)) {
            i += 1
            continue
        }

        while(i < path.length && path[i] !== "/") {
            dir += path[i]
            i++
        }

        if(dir !== "") {
            stack.push(dir)
            dir = ""
        }
    }

    return "/" + stack.join("/")
};