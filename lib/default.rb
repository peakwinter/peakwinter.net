# All files in the 'lib' directory will be loaded
# before nanoc starts compiling.

include Nanoc3::Helpers::Blogging
include Nanoc3::Helpers::Tagging
include Nanoc3::Helpers::Rendering
include Nanoc3::Helpers::LinkTo

def articles_by_year
  hash = Hash.new { |h, k| h[k] = [] }
  sorted_articles.inject(hash) do |output, post|
    year = attribute_to_time(post[:created_at]).year
    output[year] << post
    output
  end
end

def related_articles
  articles = []
  if item[:tags] != nil
    @item[:tags].each do | tag|
      @items.each do |item|
        if item[:tags] != nil and item[:tags].include? tag
          article = (articles.select { |a| a[:item] == item }).first
          if article == nil
            article = { :item => item }
            articles << article
          end
          article[:count] = (article[:count] || 0) + 1
        end
      end
    end
    # Sort the articles list by the number of tags they share
    articles.sort! { |a, b| b[:count] <=> a[:count] }
    # Ignore any items which don't share more than two tags
    articles.reject! { |a| a[:count] < 2 }
    # Only return the items
    articles.collect! { |a| a[:item] }  
  end
  articles
end

module TagItems
  def create_tag_items
    require 'set'

    tags = Set.new
    items.each do |item|
      item[:tags].each { |t| tags.add(t) } unless item[:tags].nil?
    end

    tags.each do |tag|
      @items << Nanoc::Item.new('', { :tag => tag, :title => "Articles about &ldquo;#{tag}&rdquo;" }, "/tags/#{tag}")
    end
  end
end

include TagItems

def get_post_start(post)
  content = post.compiled_content
  if content =~ /\s<!-- more -->\s/
    content = content.partition('<!-- more -->').first +
    "<div class='read-more'><a href='#{post.path}'>... Read more &#187;</a></div>"
  end
  return content
end

def get_pretty_date(post)
  attribute_to_time(post[:created_at]).strftime('%-d %B %Y')
end

