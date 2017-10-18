// 生成 doc
const fs = require('fs')
const DOC_DIR = 'doc'
const cache = []

const ignore = ['build.js', 'README.md']

const promisefy = fn => (...args) => {
  return new Promise((resolve, reject) => {
    fn(...args, (err, data) => {
      if (err) reject(err)
      else resolve(data)
    })
  })
}

const rm = path => {
  if (fs.existsSync(path)) {
    const files = fs.readdirSync(path)
    files.forEach(f => {
      const curPath = `${path}/${f}`
      if (fs.statSync(curPath).isDirectory()) {
        rm(curPath)
      } else {
        fs.unlinkSync(curPath)
      }
    })
    fs.rmdirSync(path)
  }
}
// 删除 doc 目录
rm(`./${DOC_DIR}`)

async function writeDoc() {
  await promisefy(fs.mkdir)(DOC_DIR)
  let files = await promisefy(fs.readdir)(__dirname)
  // 过滤包含文档的文件夹
  files = files.filter(f => /$cp/.test(f))
  

}
writeDoc()



