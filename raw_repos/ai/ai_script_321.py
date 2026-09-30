require 'openssl'
require 'base64'

def aes_encrypt(data, key)
  aes = OpenSSL::Cipher::AES.new(256, :ECB)
  aes.encrypt
  aes.key = key

  encrypted_data = aes.update(data) + aes.final
  Base64.encode64(encrypted_data).gsub("\n", '')
end

puts aes_encrypt("Hello, I'm a secret message to be encrypted!", '1234567890123456')