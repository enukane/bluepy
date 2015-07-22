require "json"
require "socket"


SOCKPATH="/tmp/ble.sock"

json = nil
UNIXSocket.open(SOCKPATH) do |sock|
  json = sock.readline.chomp!
end

print JSON.pretty_generate(JSON.parse(json))
