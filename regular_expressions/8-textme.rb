#!/usr/bin/env ruby

matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

puts matches.map { |m| "#{m[0]},#{m[1]},#{m[2]}" }.join