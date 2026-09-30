import Foundation

let url = URL(string: "https://my-api.com/endpoint")!

let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
  guard let data = data else { return }

  do {
    let json = try JSONSerialization.jsonObject(with: data, options: [])
    print(json)
  } catch {
    print(error)
  }
}

task.resume()