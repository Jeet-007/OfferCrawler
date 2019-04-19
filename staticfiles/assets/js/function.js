function filter(page_no) {
  product_category = document.getElementById("product_type").value;
  coupon_type = document.getElementById("coupon_type").value;
  window.location.href ="?page_no="+encodeURIComponent(page_no)+"&product_category="+encodeURIComponent(product_category)+"&coupon_type="+encodeURIComponent(coupon_type);
}