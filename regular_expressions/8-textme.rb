#!/usr/bin/env ruby
log_line = ARGV[0]
match = log_line.match(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/)
puts "#{match[1]},#{match[2]},#{match[3]}"
